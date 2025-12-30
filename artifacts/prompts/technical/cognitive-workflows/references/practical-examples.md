# Practical Examples

Real-world applications of cognitive workflow patterns.

---

## Example 1: Job Offer Evaluation (Parallel + Chain)

**Context:** Evaluating a job offer with multiple factors to consider.

### Step 1: Parallel Analysis

```xml
<parallel_analysis topic="Senior ML Engineer at TechCorp - $180k remote">

  <perspective name="Financial">
    Base: $180k (above target of $5k/mo = $60k)
    Equity: 0.1% (4-year vest) - potential upside
    Benefits: Standard (health, 401k match)
    Location arbitrage: Remote from Brazil = high purchasing power
    Score: 9/10
  </perspective>

  <perspective name="Technical">
    Stack: Python, PyTorch, Kubernetes - strong alignment
    Challenge: Production ML systems at scale - matches goals
    Team: Senior-heavy, learning opportunity
    Tech debt: Unknown - flag for interview
    Score: 8/10
  </perspective>

  <perspective name="Career">
    Brand recognition: Series C startup, growing
    Role scope: IC with tech lead path
    Timeline: Aligns with post-graduation (March 2026)
    Exit options: Strong ML experience = portable
    Score: 8/10
  </perspective>

  <perspective name="Personal">
    Remote: Full remote - ideal for Muzambinho
    Timezone: PST overlap required (evening calls)
    Travel: Quarterly - manageable
    Values: B2B SaaS, neutral on mission
    Score: 7/10
  </perspective>

</parallel_analysis>
```

### Step 2: Chain Synthesis

```
Step 1: Weight perspectives
Financial (30%) × 9 = 2.7
Technical (30%) × 8 = 2.4
Career (25%) × 8 = 2.0
Personal (15%) × 7 = 1.05
Total: 8.15/10

Step 2: Identify blockers
- No blockers identified
- Minor concern: timezone overlap

Step 3: Compare to alternatives
- Current best alternative: None (job searching)
- Opportunity cost: Low

Step 4: Decision
RECOMMEND: Accept, negotiate equity if possible
Rationale: Strong financial fit, technical alignment,
career growth potential. Minor timezone inconvenience
is acceptable trade-off.
```

---

## Example 2: Architecture Decision (Orchestrator-Workers)

**Context:** Choosing between microservices vs monolith for new project.

### Orchestrator Analysis

```xml
<orchestrator task="Architecture decision: Cidadão.AI v2">

  <analysis>
    Current state: Monolith with 22 agents
    Pain points: Scaling individual agents, deployment coupling
    Team size: 1 developer (solo)
    Timeline: 3 months to production

    Key question: Microservices worth the complexity?
  </analysis>

  <task_breakdown>
    <subtask type="monolith-advocate">
      Argue for keeping/improving monolith architecture.
      Consider: simplicity, deployment, debugging, solo dev reality.
    </subtask>

    <subtask type="microservices-advocate">
      Argue for migrating to microservices.
      Consider: scaling, isolation, future team growth.
    </subtask>

    <subtask type="hybrid-architect">
      Propose middle-ground approach.
      Consider: modular monolith, selective extraction.
    </subtask>
  </task_breakdown>

</orchestrator>
```

### Worker Outputs

```xml
<worker type="monolith-advocate">
  <response>
    KEEP MONOLITH

    Arguments:
    1. Solo developer - can't maintain N services
    2. 22 agents share significant code (LLM clients, DB)
    3. Current pain is premature optimization
    4. Deployment simplicity = faster iteration

    Recommendation: Improve internal modularity instead
    - Clean module boundaries
    - Shared nothing between agent domains
    - Single deployment, logical separation
  </response>
</worker>

<worker type="microservices-advocate">
  <response>
    MIGRATE TO MICROSERVICES

    Arguments:
    1. Agents have different scaling needs (Zumbi heavy, others light)
    2. Failure isolation prevents cascade
    3. Future team can own individual services
    4. Cloud-native = better observability

    Migration path:
    - Extract most critical agent (Zumbi) first
    - Keep others in monolith
    - Gradual strangler pattern
  </response>
</worker>

<worker type="hybrid-architect">
  <response>
    MODULAR MONOLITH (RECOMMENDED)

    Best of both worlds:
    1. Single deployment (solo dev friendly)
    2. Strong module boundaries (future extraction ready)
    3. Shared infrastructure (DRY)
    4. Agent isolation via async queues

    Implementation:
    - Domain-driven modules: /agents/zumbi, /agents/anita
    - Shared kernel: /core/llm, /core/db, /core/observability
    - Internal message bus for agent communication
    - Feature flags for gradual rollout

    Future-proof: Can extract to services when team grows
  </response>
</worker>
```

### Synthesis

```
DECISION: Modular Monolith

Rationale:
- Matches current team size (1 dev)
- Preserves simplicity while enabling future scaling
- Low risk, high optionality

Implementation priority:
1. Refactor to clean module boundaries
2. Add internal message bus
3. Document extraction points for future

Review trigger: When team > 3 or specific agent needs independent scaling
```

---

## Example 3: Bug Triage (Route)

**Context:** Incoming bug report needs appropriate handling.

```xml
<router input="Users report 500 errors on /api/agents/zumbi endpoint">

  <classify>
    <reasoning>
      - 500 error = server-side failure
      - Specific endpoint = isolated issue
      - User-reported = production impact
      - Critical path (Zumbi is main agent)
    </reasoning>

    <severity>P1 - Critical</severity>
    <category>production-incident</category>
  </classify>

  <route category="production-incident">
    INCIDENT RESPONSE PROTOCOL

    1. IMMEDIATE (< 5 min)
       - Check error logs: `kubectl logs -l app=cidadao-api`
       - Verify DB connectivity
       - Check LLM provider status

    2. DIAGNOSE (< 15 min)
       - Reproduce locally if possible
       - Identify root cause
       - Assess blast radius

    3. MITIGATE (< 30 min)
       - Implement fix OR
       - Rollback to last known good OR
       - Enable fallback/degraded mode

    4. COMMUNICATE
       - Update status page
       - Notify stakeholders

    5. POST-MORTEM
       - Document timeline
       - Identify prevention measures
       - Update monitoring/alerts
  </route>

</router>
```

---

## Example 4: Code Quality Check (Evaluator-Optimizer)

**Context:** Ensuring PR meets quality standards before merge.

```xml
<iteration_loop task="Review PR #123: Add rate limiting to API">

  <generate iteration="1">
    Initial review of changes:

    Files changed:
    - api/middleware/rate_limit.py (new)
    - api/routes/agents.py (modified)
    - tests/test_rate_limit.py (new)

    Initial assessment:
    - Implementation uses token bucket algorithm ✓
    - Configurable limits per endpoint ✓
    - Redis backend for distributed limiting ✓
  </generate>

  <evaluate iteration="1">
    Criteria scores:

    - Correctness: 4/5
      Missing: Edge case for Redis connection failure

    - Performance: 5/5
      O(1) operations, minimal overhead

    - Security: 3/5
      Missing: IP spoofing protection (X-Forwarded-For)

    - Tests: 3/5
      Missing: Integration tests, load tests

    - Documentation: 2/5
      Missing: README update, configuration docs

    Overall: FAIL (Security < 4, Tests < 4, Docs < 4)

    Required improvements:
    1. Add Redis connection fallback
    2. Validate X-Forwarded-For header
    3. Add integration test with Redis
    4. Document configuration options
  </evaluate>

  <optimize iteration="2">
    Requested changes from author:

    1. ✓ Added try/except with fallback to in-memory limiting
    2. ✓ Added IP validation middleware
    3. ✓ Added integration test (test_rate_limit_redis.py)
    4. ✓ Added docs/RATE_LIMITING.md
  </optimize>

  <evaluate iteration="2">
    Re-evaluation:

    - Correctness: 5/5 ✓
    - Performance: 5/5 ✓
    - Security: 5/5 ✓
    - Tests: 4/5 ✓
    - Documentation: 4/5 ✓

    Overall: PASS

    Minor suggestions (non-blocking):
    - Consider adding Prometheus metrics for rate limit hits
    - Add example curl commands to docs
  </evaluate>

  <result>
    Status: APPROVED
    Comments: Well-implemented rate limiting with good test coverage.
    Suggestions provided for future enhancement.
  </result>

</iteration_loop>
```

---

## Pattern Selection Heuristic

```
IF task is sequential transformation
   → Use CHAIN

IF task needs multiple viewpoints
   → Use PARALLEL

IF task type determines approach
   → Use ROUTE

IF subtasks are unknown upfront
   → Use ORCHESTRATOR

IF quality requires iteration
   → Use EVALUATOR

IF complex with mixed needs
   → COMBINE patterns
```

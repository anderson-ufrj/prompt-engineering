# Prompt Engineering Lab - Restructure Plan

## Theme: Master Craftsmen & Inventors

Transform prompts into masterpieces through the wisdom of history's greatest artisans.

---

## 0. CRITICAL: Preserve Existing Infrastructure

**The new structure is an ORCHESTRATION LAYER on top of existing code, NOT a replacement.**

### Existing Python Infrastructure (DO NOT MODIFY)
```
/
├── setup.py                        # Project setup
├── integration_pipeline.py         # Main integration script
├── requirements.txt                # Dependencies
│
├── anderson_skill/                 # Python module for versioning
│   ├── __init__.py
│   └── meta/
│       ├── __init__.py
│       └── version_manager.py
│
├── evidence/                       # Metrics & research system
│   ├── __init__.py
│   ├── dashboard.py                # Visualization
│   ├── auto_calibration.py         # Auto-calibration
│   ├── metrics/
│   │   ├── __init__.py
│   │   └── interaction_analyzer.py # Core metrics
│   ├── patterns/                   # Extracted patterns
│   └── sources/                    # External references (anthropic-cookbook, etc.)
│
├── experiments/                    # A/B testing framework
│   ├── __init__.py
│   └── experiment_runner.py
│
├── tests/                          # Test suite (7 files, >76% coverage target)
│   ├── test_experiment_runner.py
│   ├── test_integration_real_data.py
│   ├── test_interaction_analyzer.py
│   ├── test_version_manager.py
│   ├── test_dashboard.py
│   └── test_integration_pipeline.py
│
├── skills/                         # Detailed skills with Python scripts
│   ├── dsr/                        # Design Science Research
│   ├── cognitive-workflows/        # Multi-LLM patterns
│   ├── document-skills/            # PDF, DOCX, PPTX processing (Python)
│   ├── slack-gif-creator/          # GIF creation (Python)
│   └── [other skills...]
│
├── anderson-skill/                 # Personal meta-skill (WHO + HOW)
│   ├── SKILL.md
│   ├── core/
│   ├── dynamic/
│   └── contexts/
│
└── prompts/                        # Legacy prompts
```

---

## 1. Target Structure (NEW Layer + Existing)

```
/
├── AI.md                           <-- THE MAP (Entry Point)
│                                       "Read Constitution, then choose a Sub-Agent"
│
├── .agent/                         <-- ORCHESTRATION LAYER (NEW)
│   ├── skills/                     <-- ATOMIC SKILLS (References to detailed skills)
│   │   ├── git.md                  "Standard Git commands"
│   │   ├── test.md                 "References → experiments/, tests/"
│   │   ├── metrics.md              "References → evidence/metrics/"
│   │   └── review-checklist.md     "PR review standards"
│   │
│   ├── workflows/                  <-- PROCESS ORCHESTRATION (How to combine)
│   │   ├── feature-dev.md          "Plan → Code → Test (uses experiments/)"
│   │   ├── bug-fix.md              "Reproduce → Fix → Verify (uses tests/)"
│   │   ├── deploy.md               "Lint → Build → Ship"
│   │   └── pr-review.md            "Fetch → Review → Approve"
│   │
│   └── sub-agents/                 <-- PERSONAS (Craftsmen Roles)
│       ├── davinci.md              "The Polymath - Tech Lead"
│       ├── gutenberg.md            "The Publisher - Documentarian"
│       ├── tesla.md                "The Automator - DevOps"
│       ├── stradivari.md           "The Perfectionist - QA Engineer"
│       └── michelangelo.md         "The Sculptor - Code Reviewer"
│
├── .specify/
│   └── memory/                     <-- GOVERNANCE (NEW)
│       ├── constitution.md         "The Law - Tech Stack & Rules (4D Framework)"
│       └── plan.md                 "Current Task List"
│
├── .cursorrules                    <-- POINTER: "Read /AI.md first"
├── .clinerules                     <-- POINTER: "Read /AI.md first"
├── GEMINI.md                       <-- POINTER: "Read /AI.md first"
│
└── [ALL EXISTING DIRECTORIES PRESERVED - see section 0]
```

---

## 2. Craftsmen Personas (Sub-Agents)

### 2.1 Da Vinci - The Polymath (Tech Lead)
**Role:** Architecture, system design, holistic thinking
**4D Focus:** Delegation (deciding what to build)
**Workflow:** `pr-review.md`

> "Simplicity is the ultimate sophistication."

**Capabilities:**
- System architecture decisions
- Code review with architectural lens
- Cross-cutting concerns (security, performance)
- Technical debt assessment

---

### 2.2 Gutenberg - The Publisher (Documentarian)
**Role:** Documentation, knowledge preservation, communication
**4D Focus:** Description (articulating clearly)
**Workflow:** `feature-dev.md` (documentation phase)

> "Knowledge must be shared to have value."

**Capabilities:**
- Technical documentation
- API documentation
- README creation
- Knowledge base maintenance

---

### 2.3 Tesla - The Automator (DevOps Engineer)
**Role:** Automation, CI/CD, infrastructure
**4D Focus:** Diligence (reliable, responsible systems)
**Workflow:** `deploy.md`

> "If you want to find the secrets of the universe, think in terms of energy, frequency and vibration."

**Capabilities:**
- CI/CD pipeline management
- Infrastructure as Code
- Deployment automation
- Monitoring and alerting

---

### 2.4 Stradivari - The Perfectionist (QA Engineer)
**Role:** Quality assurance, testing, precision
**4D Focus:** Discernment (evaluating outputs carefully)
**Workflow:** `bug-fix.md`, `test.md`

> "Perfection is achieved not when there is nothing more to add, but when there is nothing left to take away."

**Capabilities:**
- Test strategy design
- Bug reproduction and analysis
- Quality metrics
- Edge case identification

---

### 2.5 Michelangelo - The Sculptor (Code Reviewer)
**Role:** Code refinement, beauty in code, craftsmanship
**4D Focus:** Discernment + Description
**Workflow:** `pr-review.md`, `review-checklist.md`

> "I saw the angel in the marble and carved until I set him free."

**Capabilities:**
- Code review with craftsmanship focus
- Refactoring recommendations
- Code aesthetics and readability
- Pattern identification

---

## 3. 4D Framework Integration

### Constitution Structure (`.specify/memory/constitution.md`)

```
4D FRAMEWORK GOVERNANCE
=======================

## DELEGATION - What should AI do vs. Human?
- AI handles: repetitive tasks, pattern matching, boilerplate
- Human decides: architecture, business logic, ethics
- Escalation rules: when to ask for human input

## DESCRIPTION - How to communicate clearly?
- Use structured prompts
- Provide context before request
- Include examples when possible
- State constraints explicitly

## DISCERNMENT - How to evaluate AI output?
- Review against acceptance criteria
- Check for edge cases
- Validate against existing patterns
- Test before merging

## DILIGENCE - Ethical and responsible use?
- No secrets in prompts
- Credit sources appropriately
- Maintain human oversight
- Document AI-assisted decisions
```

---

## 4. Workflow Details

### 4.1 feature-dev.md
```
Step 1: PLAN (Da Vinci leads)
  - Define requirements
  - Design architecture
  - Identify risks

Step 2: CODE (Human + AI collaboration)
  - Implement using skills
  - Follow constitution rules

Step 3: TEST (Stradivari validates)
  - Run test suite
  - Verify acceptance criteria
```

### 4.2 bug-fix.md
```
Step 1: REPRODUCE (Stradivari investigates)
  - Identify reproduction steps
  - Document expected vs actual

Step 2: FIX (Apply relevant skill)
  - Implement fix
  - Add regression test

Step 3: VERIFY (Stradivari confirms)
  - Run full test suite
  - Confirm fix works
```

### 4.3 deploy.md
```
Step 1: LINT (Automated checks)
  - Code style
  - Type checking
  - Security scan

Step 2: BUILD (Tesla orchestrates)
  - Compile/bundle
  - Run tests
  - Generate artifacts

Step 3: SHIP (Tesla deploys)
  - Deploy to environment
  - Verify health
  - Monitor metrics
```

### 4.4 pr-review.md
```
Step 1: FETCH (Get PR context)
  - Read PR description
  - Understand scope

Step 2: REVIEW (Michelangelo + Da Vinci)
  - Apply review-checklist.md
  - Check architecture alignment
  - Verify code quality

Step 3: APPROVE (Final decision)
  - Approve or request changes
  - Document feedback
```

---

## 5. Migration Plan

### Phase 1: Structure Creation
- [x] Create `.agent/` directory tree
- [ ] Create `.specify/memory/` directory
- [ ] Create pointer files

### Phase 2: Core Files
- [ ] Write `AI.md` (entry point with 4D)
- [ ] Write `constitution.md` (governance)
- [ ] Write `plan.md` (task template)

### Phase 3: Skills Migration
- [ ] Create atomic skills in `.agent/skills/`
- [ ] Map existing skills from `skills/` folder

### Phase 4: Workflows
- [ ] Create all workflow files
- [ ] Link workflows to skills

### Phase 5: Sub-Agents (Craftsmen)
- [ ] Create Da Vinci persona
- [ ] Create Gutenberg persona
- [ ] Create Tesla persona
- [ ] Create Stradivari persona
- [ ] Create Michelangelo persona

### Phase 6: Integration
- [ ] Update AGENTS.md to reference new structure
- [ ] Create pointer files
- [ ] Test full flow

---

## 6. Integration: Craftsmen → Python Modules

Each craftsman persona REFERENCES and ORCHESTRATES the existing Python infrastructure:

### Stradivari (QA Engineer) → Tests & Experiments
```
stradivari.md references:
├── tests/                          # Run with: pytest tests/
│   ├── test_experiment_runner.py
│   ├── test_interaction_analyzer.py
│   └── ...
├── experiments/                    # Run with: python experiments/experiment_runner.py
│   └── experiment_runner.py
└── evidence/metrics/               # Analyze with: python -c "from evidence.metrics import *"
    └── interaction_analyzer.py
```

### Tesla (DevOps) → Setup & Pipeline
```
tesla.md references:
├── setup.py                        # Run with: python setup.py install
├── integration_pipeline.py         # Run with: python integration_pipeline.py
└── requirements.txt                # Run with: pip install -r requirements.txt
```

### Gutenberg (Documentarian) → Evidence & Patterns
```
gutenberg.md references:
├── evidence/patterns/              # Documented patterns
├── evidence/sources/               # Research materials
├── docs/                           # Project documentation
└── skills/dsr/                     # Design Science Research methodology
```

### Da Vinci (Tech Lead) → Architecture Overview
```
davinci.md references:
├── AGENTS.md                       # Current architecture
├── anderson-skill/                 # Personal context system
├── skills/cognitive-workflows/     # Multi-LLM patterns
└── evidence/patterns/              # Architectural patterns
```

### Michelangelo (Code Reviewer) → Quality Standards
```
michelangelo.md references:
├── .agent/skills/review-checklist.md
├── tests/                          # Must pass before merge
└── evidence/patterns/              # Follow established patterns
```

---

## 7. Relationship to Existing Structure

| Current | Action | Integration |
|---------|--------|-------------|
| `tests/` | KEEP | Stradivari executes `pytest tests/` |
| `experiments/` | KEEP | Stradivari runs experiments |
| `evidence/` | KEEP | Gutenberg documents, Tesla monitors |
| `skills/` | KEEP | Referenced by `.agent/skills/` |
| `anderson-skill/` | KEEP | Load alongside constitution |
| `anderson_skill/` | KEEP | Python module for versioning |
| `setup.py` | KEEP | Tesla runs setup |
| `integration_pipeline.py` | KEEP | Tesla orchestrates pipeline |
| `AGENTS.md` | KEEP | Update to reference AI.md |

---

## 8. Success Criteria

1. **Zero Breakage:** All existing tests pass after restructure
2. **Clear Entry Point:** AI.md provides unambiguous starting point
3. **4D Integration:** Each component maps to a 4D competency
4. **Persona Coherence:** Each craftsman has distinct role and voice
5. **Python Integration:** Craftsmen reference real Python modules
6. **Workflow Clarity:** Each workflow has clear steps with executable commands

---

## 9. Verification Commands

After restructure, verify everything works:

```bash
# 1. Tests still pass
pytest tests/ -v

# 2. Python imports work
python -c "from evidence.metrics import interaction_analyzer; print('OK')"
python -c "from experiments import experiment_runner; print('OK')"
python -c "from anderson_skill.meta import version_manager; print('OK')"

# 3. Setup still works
python setup.py --version

# 4. New structure exists
ls -la .agent/skills/ .agent/workflows/ .agent/sub-agents/
ls -la .specify/memory/
cat AI.md | head -20
```

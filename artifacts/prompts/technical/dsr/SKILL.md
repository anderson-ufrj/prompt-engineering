---
name: dsr
description: |
  Design Science Research Methodology for rigorous artifact development. Use this skill when:
  (1) Creating new tools, frameworks, or systems that solve real problems
  (2) Need structured approach to build-evaluate-iterate cycles
  (3) Want scientific rigor in development process
  (4) Evaluating artifacts against clear criteria
  (5) Documenting research contributions systematically

  Based on Hevner et al. (2004) and Peffers et al. (2007) - foundational DSR papers.
---

# Design Science Research (DSR)

A scientific methodology for creating and evaluating IT artifacts that solve real problems.

## Quick Reference

| Activity | Question | Output |
|----------|----------|--------|
| **1. Problem** | What problem needs solving? | Problem statement, motivation |
| **2. Objectives** | What would a solution look like? | Requirements, success criteria |
| **3. Design** | How do we build it? | Artifact architecture |
| **4. Demonstration** | Does it work? | Working prototype |
| **5. Evaluation** | How well does it work? | Metrics, comparison |
| **6. Communication** | Who needs to know? | Documentation, papers |

---

## The DSRM Process Model

```
┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
│ 1.       │   │ 2.       │   │ 3.       │   │ 4.       │   │ 5.       │   │ 6.       │
│ Problem  │──►│Objectives│──►│ Design & │──►│ Demon-   │──►│ Evaluate │──►│Communi-  │
│ Identify │   │          │   │ Develop  │   │ strate   │   │          │   │ cate     │
└──────────┘   └──────────┘   └──────────┘   └──────────┘   └──────────┘   └──────────┘
     │                             ▲              │              │
     │                             │              └──────────────┘
     │                             │                 (iterate)
     └─────────────────────────────┘
              (refine problem understanding)
```

---

## Activity 1: Problem Identification & Motivation

### Purpose
Define the research problem and justify the value of a solution.

### Questions to Answer
- What is the problem?
- Why is it important?
- Who is affected?
- What is the current state?
- What are the consequences of not solving it?

### Template

```xml
<problem_identification>
  <problem_statement>
    [Clear, concise statement of the problem]
  </problem_statement>

  <importance>
    [Why does this matter? Quantify if possible]
  </importance>

  <stakeholders>
    [Who is affected by this problem?]
  </stakeholders>

  <current_state>
    [How is this currently handled? What are the limitations?]
  </current_state>

  <consequences>
    [What happens if we don't solve this?]
  </consequences>
</problem_identification>
```

### Example

```xml
<problem_identification>
  <problem_statement>
    Human-AI collaboration lacks personalization, leading to repetitive
    context-setting and suboptimal interactions.
  </problem_statement>

  <importance>
    Developers spend 15-30% of AI interaction time re-establishing context.
    This reduces productivity and leads to frustration.
  </importance>

  <stakeholders>
    - Developers using AI assistants
    - Teams adopting AI-augmented workflows
    - Organizations investing in AI tools
  </stakeholders>

  <current_state>
    - Generic system prompts used for all users
    - No persistent memory of user preferences
    - Context lost between sessions
  </current_state>

  <consequences>
    - Continued inefficiency in human-AI collaboration
    - Slower AI adoption due to friction
    - Missed potential of personalized AI assistance
  </consequences>
</problem_identification>
```

---

## Activity 2: Define Objectives of a Solution

### Purpose
Infer objectives from the problem definition and knowledge of what is possible.

### Questions to Answer
- What would an ideal solution do?
- What are the success criteria?
- How will we know if we've succeeded?
- What constraints must we respect?

### Template

```xml
<objectives>
  <ideal_solution>
    [Description of what success looks like]
  </ideal_solution>

  <success_criteria>
    <criterion metric="[metric_name]">
      [Specific, measurable criterion]
    </criterion>
    <!-- Add more criteria -->
  </success_criteria>

  <constraints>
    <constraint type="technical">[constraint]</constraint>
    <constraint type="resource">[constraint]</constraint>
    <constraint type="time">[constraint]</constraint>
  </constraints>

  <non_goals>
    [What are we explicitly NOT trying to achieve?]
  </non_goals>
</objectives>
```

### Objective Types

| Type | Description | Example |
|------|-------------|---------|
| **Quantitative** | Measurable numbers | "Reduce context-setting time by 50%" |
| **Qualitative** | Observable improvements | "Users report higher satisfaction" |
| **Comparative** | Better than alternatives | "Outperform baseline approach" |
| **Satisficing** | Meet minimum threshold | "Achieve 80% accuracy" |

---

## Activity 3: Design & Development

### Purpose
Create the artifact - constructs, models, methods, or instantiations.

### Artifact Types

| Type | Description | Examples |
|------|-------------|----------|
| **Constructs** | Vocabulary, concepts | DMMF dimensions, pattern names |
| **Models** | Abstractions, representations | Architecture diagrams, frameworks |
| **Methods** | Algorithms, processes | Workflow patterns, evaluation procedures |
| **Instantiations** | Working systems | Implemented software, prototypes |

### Template

```xml
<design>
  <artifact_type>[construct|model|method|instantiation]</artifact_type>

  <architecture>
    [High-level design of the artifact]
  </architecture>

  <components>
    <component name="[name]">
      <purpose>[what it does]</purpose>
      <interface>[how to interact with it]</interface>
    </component>
  </components>

  <design_decisions>
    <decision>
      <choice>[what was decided]</choice>
      <rationale>[why this choice]</rationale>
      <alternatives>[what else was considered]</alternatives>
    </decision>
  </design_decisions>

  <theoretical_foundation>
    [What theories/prior work inform this design?]
  </theoretical_foundation>
</design>
```

### Design Principles (Hevner's Guidelines)

1. **Artifact Focus** - Produce something concrete and usable
2. **Problem Relevance** - Solve a real problem that matters
3. **Rigor** - Apply appropriate theoretical foundations
4. **Search Process** - Iterate through solution space systematically

---

## Activity 4: Demonstration

### Purpose
Demonstrate use of the artifact to solve the problem.

### Demonstration Methods

| Method | Use Case | Example |
|--------|----------|---------|
| **Proof of Concept** | Show feasibility | Minimal working implementation |
| **Case Study** | Real-world application | Apply to actual project |
| **Simulation** | Controlled testing | Run with synthetic data |
| **Experiment** | Comparative evaluation | A/B test with alternatives |

### Template

```xml
<demonstration>
  <method>[proof_of_concept|case_study|simulation|experiment]</method>

  <context>
    [Where/how is the artifact being demonstrated?]
  </context>

  <scenario>
    <input>[what goes in]</input>
    <process>[what happens]</process>
    <output>[what comes out]</output>
  </scenario>

  <observations>
    [What did we observe during demonstration?]
  </observations>

  <artifacts_produced>
    [What tangible outputs were created?]
  </artifacts_produced>
</demonstration>
```

---

## Activity 5: Evaluation

### Purpose
Observe and measure how well the artifact supports a solution.

### Evaluation Methods

| Category | Method | Description |
|----------|--------|-------------|
| **Observational** | Case Study | In-depth analysis of real use |
| **Observational** | Field Study | Natural environment observation |
| **Analytical** | Static Analysis | Examine structure/properties |
| **Analytical** | Architecture Analysis | Evaluate design qualities |
| **Experimental** | Controlled Experiment | Isolate variables |
| **Experimental** | Simulation | Model-based testing |
| **Testing** | Functional Testing | Does it work correctly? |
| **Testing** | Structural Testing | Code coverage, paths |
| **Descriptive** | Informed Argument | Logical reasoning |
| **Descriptive** | Scenarios | Detailed use cases |

### Template

```xml
<evaluation>
  <method>[evaluation method]</method>

  <criteria>
    <criterion name="[name]" weight="[0-1]">
      <definition>[what does this measure?]</definition>
      <measurement>[how do we measure it?]</measurement>
      <threshold>[what counts as success?]</threshold>
    </criterion>
  </criteria>

  <results>
    <result criterion="[name]">
      <score>[actual measurement]</score>
      <evidence>[supporting data]</evidence>
    </result>
  </results>

  <analysis>
    [Interpretation of results]
  </analysis>

  <limitations>
    [What are the limitations of this evaluation?]
  </limitations>

  <improvements>
    [What could be improved based on evaluation?]
  </improvements>
</evaluation>
```

### Evaluation Checklist

- [ ] Are criteria aligned with objectives?
- [ ] Is evidence quantifiable where possible?
- [ ] Are limitations acknowledged?
- [ ] Is comparison to alternatives included?
- [ ] Are threats to validity addressed?

---

## Activity 6: Communication

### Purpose
Communicate the problem, artifact, and results to relevant audiences.

### Audiences

| Audience | Focus | Format |
|----------|-------|--------|
| **Researchers** | Methodology, rigor, contribution | Academic paper |
| **Practitioners** | How to use, benefits | Documentation, tutorials |
| **Management** | Business value, ROI | Executive summary |
| **Community** | Accessibility, adoption | Blog posts, talks |

### Template

```xml
<communication>
  <audience>[target audience]</audience>

  <key_messages>
    <message priority="1">[most important takeaway]</message>
    <message priority="2">[second takeaway]</message>
    <message priority="3">[third takeaway]</message>
  </key_messages>

  <contribution_type>
    [artifact|foundation|methodology]
  </contribution_type>

  <artifacts>
    <artifact type="[type]" location="[where]">
      [description]
    </artifact>
  </artifacts>

  <reproducibility>
    [How can others reproduce/build on this work?]
  </reproducibility>
</communication>
```

---

## Hevner's 7 Guidelines Checklist

Use this to validate your DSR project:

| # | Guideline | Question | Status |
|---|-----------|----------|--------|
| 1 | **Design as Artifact** | Did we create a concrete artifact? | [ ] |
| 2 | **Problem Relevance** | Does it solve a real problem? | [ ] |
| 3 | **Design Evaluation** | Did we rigorously evaluate it? | [ ] |
| 4 | **Research Contributions** | What's new/novel? | [ ] |
| 5 | **Research Rigor** | Did we apply appropriate methods? | [ ] |
| 6 | **Design as Search** | Did we explore the solution space? | [ ] |
| 7 | **Communication** | Did we share with relevant audiences? | [ ] |

---

## Entry Points

You can enter the DSRM process at different points:

| Entry Point | Trigger | Start At |
|-------------|---------|----------|
| **Problem-Centered** | New problem identified | Activity 1 |
| **Objective-Centered** | Industry/research need | Activity 2 |
| **Design-Centered** | Existing artifact to extend | Activity 3 |
| **Client-Centered** | Consulting engagement | Activity 4 |

---

## Iteration Patterns

### Pattern 1: Linear
```
1 → 2 → 3 → 4 → 5 → 6
```
Use when: Problem is well-understood, single iteration sufficient.

### Pattern 2: Evaluation Loop
```
1 → 2 → 3 → 4 → 5 → (improvements) → 3 → 4 → 5 → 6
```
Use when: Iterative refinement needed based on evaluation.

### Pattern 3: Problem Refinement
```
1 → 2 → 3 → 4 → (new insights) → 1 → 2 → 3 → 4 → 5 → 6
```
Use when: Demonstration reveals problem was misunderstood.

### Pattern 4: Continuous
```
1 → 2 → 3 → 4 → 5 → 6 → (feedback) → 1 ...
```
Use when: Ongoing research program with multiple cycles.

---

## Integration with Cognitive Workflows

DSR activities can use cognitive workflow patterns:

| DSR Activity | Useful Patterns |
|--------------|-----------------|
| Problem ID | **Parallel** - Multiple stakeholder perspectives |
| Objectives | **Chain** - Problem → Constraints → Criteria |
| Design | **Orchestrator** - Break down into design tasks |
| Demonstration | **Route** - Different demo paths per audience |
| Evaluation | **Evaluator-Optimizer** - Iterative refinement |
| Communication | **Parallel** - Different audience versions |

---

## References

- Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design Science in Information Systems Research. *MIS Quarterly*, 28(1), 75-105.
- Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A Design Science Research Methodology. *JMIS*, 24(3), 45-77.

---

*Evidence: evidence/patterns/004-design-science-research-methodology.md*

# Prompt Engineering Lab

**Personal prompt engineering system for human-AI collaboration**

> A self-evolving system where prompts adapt to focus, context changes trigger prompt evolution, and evidence-based calibration ensures continuous improvement.

---

## Scientific Foundation: DMMF

This project is grounded in the **Developer Mental Model Framework (DMMF)**, a research framework for inferring cognitive patterns from repository artifacts.

| Dimension | What It Captures | Repository Manifestation |
|-----------|------------------|--------------------------|
| **Cognitive** | Problem decomposition, abstraction | Code structure, directory depth |
| **Affective** | Emotional patterns, quality drive | Commit sentiment, test coverage |
| **Conative** | Values, motivation, purpose | Project themes, documentation |
| **Reflective** | Self-correction, iteration | Refactoring patterns, commit sequences |

**Research basis:** "From Commits to Cognition: A Mixed-Methods Framework for Inferring Developer Mental Models from Repository Artifacts" (Silva, 2025)

**Empirical foundation:** 40 repositories, 2,799 commits, 3 years of longitudinal data.

---

## Philosophy

This repository implements a **scientific approach to prompt engineering**:

1. **Evidence-Based Evolution** - Every prompt change is backed by observed interaction patterns
2. **Modular Composition** - Personal context + technical skills + situational modes combine dynamically
3. **Continuous Calibration** - Good/bad interaction examples refine the system over time
4. **Version Control for Prompts** - Track prompt evolution like code, with semantic versioning

---

## Architecture

```
prompt-engineering/
│
├── README.md                    # This file
├── CHANGELOG.md                 # Version history and evolution log
│
├── anderson-skill/              # Personal meta-skill (WHO + HOW)
│   ├── SKILL.md                 # Entry point with YAML metadata
│   ├── core/                    # Stable context (identity, values, communication)
│   ├── dynamic/                 # Volatile context (goals, career status)
│   ├── contexts/                # Situational modes (debug, interview, brainstorm)
│   ├── interactions/            # Calibration examples (good/bad patterns)
│   └── meta/                    # Versioning and maintenance docs
│
├── skills/                      # Technical skills library (WHAT)
│   ├── [skill-name]/            # Each skill is self-contained
│   │   ├── SKILL.md             # Skill definition and instructions
│   │   └── [resources]/         # Scripts, templates, references
│   └── README.md                # Skills catalog and usage guide
│
├── prompts/                     # Legacy prompts (migration in progress)
│   └── [persona-prompts]/       # Historical prompt personas
│
├── experiments/                 # A/B testing and prompt experiments
│   ├── hypothesis/              # Experiment definitions
│   ├── results/                 # Measured outcomes
│   └── README.md                # Experiment methodology
│
├── evidence/                    # Interaction evidence base
│   ├── patterns/                # Recurring effective patterns
│   ├── antipatterns/            # Patterns to avoid
│   ├── metrics/                 # Quantitative measurements
│   └── sources/                 # Raw data sources (anonymized)
│
└── docs/                        # Reference materials
    ├── books/                   # Prompt engineering literature
    ├── research/                # Academic papers and articles
    └── personal/                # CV, portfolio materials
```

---

## Core Concepts

### 1. Personal Meta-Skill (`anderson-skill/`)

The foundation layer that defines:
- **Identity** - Background, values, intellectual trajectory
- **Communication Style** - Tone, depth, language preferences
- **Situational Modes** - How context changes interaction style
- **Calibration Examples** - Real interactions that worked/failed

This skill answers: *"Who am I working with and how should we communicate?"*

### 2. Technical Skills (`skills/`)

Task-specific instructions that define:
- **What** to do (capabilities, workflows)
- **How** to do it (step-by-step processes)
- **Quality criteria** (success metrics)

Skills are **composable** - combine personal context with technical skill for optimal results.

### 3. Evidence Base (`evidence/`)

Empirical foundation built from:
- **GitHub History** - Commit patterns, PR discussions, code reviews
- **Project Analysis** - What worked in real projects
- **Interaction Logs** - Effective vs ineffective AI conversations
- **Metrics** - Response quality, iteration counts, time-to-solution

### 4. Experiments (`experiments/`)

Scientific approach to prompt improvement:
- **Hypothesis** - "Adding X context will improve Y outcome"
- **Variables** - What's being tested
- **Measurement** - How success is determined
- **Results** - Documented outcomes with data

---

## How It Works

```
┌─────────────────────────────────────────────────────────────┐
│                    INTERACTION FLOW                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐  │
│  │   Context    │ +  │    Skill     │ +  │    Mode      │  │
│  │  (WHO I am)  │    │  (WHAT to do)│    │ (HOW urgent) │  │
│  └──────────────┘    └──────────────┘    └──────────────┘  │
│         │                   │                   │           │
│         └───────────────────┴───────────────────┘           │
│                             │                               │
│                             ▼                               │
│                   ┌──────────────────┐                      │
│                   │ Composed Prompt  │                      │
│                   └──────────────────┘                      │
│                             │                               │
│                             ▼                               │
│                   ┌──────────────────┐                      │
│                   │   AI Response    │                      │
│                   └──────────────────┘                      │
│                             │                               │
│                             ▼                               │
│                   ┌──────────────────┐                      │
│                   │ Evidence Capture │──────┐               │
│                   └──────────────────┘      │               │
│                                             ▼               │
│                                   ┌──────────────────┐      │
│                                   │ System Evolution │      │
│                                   └──────────────────┘      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Evidence Sources

### GitHub Analysis
- Commit message patterns and quality
- Code review discussions
- PR descriptions and rationale
- Issue resolution approaches

### Local Projects
- `cidadao.ai` - Multi-agent system patterns
- `neural-lab` - ML experimentation workflows
- `contributions` - Open source interaction styles

### Interaction History
- Effective debugging sessions
- Successful brainstorming conversations
- Failed interactions and why

---

## Usage

### For AI Assistants (Claude Code, etc.)

1. **Load personal context first** (`anderson-skill/SKILL.md`)
2. **Identify situational mode** (urgent? exploratory? technical?)
3. **Load relevant technical skill** if task-specific
4. **Adapt communication** based on context signals
5. **Contribute to evidence** when patterns emerge

### For Anderson (Maintenance)

```bash
# Update dynamic context (weekly or on change)
vim anderson-skill/dynamic/goals.md
vim anderson-skill/dynamic/career-status.md

# Add new interaction examples
vim anderson-skill/interactions/good/NNN-description.md

# Run experiment
vim experiments/hypothesis/NNN-experiment-name.md
# ... conduct experiment ...
vim experiments/results/NNN-experiment-name.md

# Version bump on significant changes
vim anderson-skill/meta/CHANGELOG.md
```

---

## Versioning

### Semantic Versioning for Prompts

- **MAJOR** (X.0.0) - Fundamental life/context change (student → employed)
- **MINOR** (0.X.0) - New skill, significant capability, career milestone
- **PATCH** (0.0.X) - Tweaks, calibration updates, minor refinements

### Current Version: 0.1.0

- Initial structure established
- Core personal context documented
- Evidence collection framework defined

---

## Roadmap

### Phase 1: Foundation (Current)
- [x] Repository structure
- [x] Personal meta-skill (`anderson-skill`)
- [x] Reference skills library
- [ ] Evidence collection framework
- [ ] Initial GitHub history analysis

### Phase 2: Evidence Base
- [ ] Analyze GitHub commit patterns
- [ ] Extract project interaction patterns
- [ ] Document effective prompting strategies
- [ ] Build antipattern library

### Phase 3: Experimentation
- [ ] A/B testing framework
- [ ] Metrics collection
- [ ] Hypothesis-driven improvements
- [ ] Automated calibration suggestions

### Phase 4: Automation
- [ ] CI/CD for prompt validation
- [ ] Automated evidence extraction
- [ ] Quality metrics dashboard
- [ ] Cross-project pattern detection

---

## Principles

### 1. Evidence Over Intuition
Every prompt decision should be traceable to observed outcomes.

### 2. Composition Over Monoliths
Small, focused modules that combine > large, rigid templates.

### 3. Evolution Over Perfection
Prompts are living documents that improve through iteration.

### 4. Transparency Over Magic
Document WHY prompts work, not just WHAT they contain.

### 5. Personal Over Generic
This system is optimized for one human-AI partnership, not universal use.

---

## License

**Proprietary - All Rights Reserved**

This repository contains personal context, communication preferences, and proprietary prompt engineering strategies. Not open source.

For inquiries: andersonhs27@gmail.com

---

## Author

**Anderson Henrique da Silva**
- Location: Minas Gerais, Brasil
- Background: Philosophy → Computer Science
- Focus: AI/ML Engineering, Multi-Agent Systems, AI Safety

---

*Last Updated: 2025-12-30*
*Next Review: After thesis defense (December 2025)*

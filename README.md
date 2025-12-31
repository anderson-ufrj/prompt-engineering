# Prompt Engineering Lab

**Author:** Anderson Henrique da Silva
**Location:** Minas Gerais, Brasil

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
├── AI.md                        # Entry point for AI assistants
├── README.md                    # This file
│
├── anderson-skill/              # Personal meta-skill (WHO + HOW)
│   ├── SKILL.md                 # Entry point
│   ├── core/                    # Stable context (identity, communication)
│   ├── dynamic/                 # Volatile context (goals, status)
│   ├── contexts/                # Situational modes (debug, brainstorm)
│   ├── interactions/            # Calibration examples (good/bad)
│   └── meta/                    # Versioning metadata
│
├── artifacts/                   # Produced artifacts
│   ├── agents/                  # Brazilian AI agent personas
│   ├── prompts/                 # Prompt templates and skills
│   └── workflows/               # Orchestrated processes
│
├── src/                         # Python source code
│   ├── analysis/                # Data analysis scripts
│   ├── calibration/             # Dashboard and auto-calibration
│   ├── experiments/             # A/B testing framework
│   ├── import/                  # Data importers
│   ├── metrics/                 # Metrics collection
│   ├── pipeline/                # Component orchestration
│   └── versioning/              # Version management
│
├── evidence/                    # Interaction evidence base
│   ├── analysis/                # Analysis results
│   ├── antipatterns/            # Patterns to avoid
│   ├── metrics/                 # Quantitative measurements (local only)
│   ├── models/                  # Analysis models
│   ├── patterns/                # Recurring effective patterns
│   └── sources/                 # External sources (anthropic-cookbook, etc.)
│
├── experiments/                 # A/B testing and experiments
│   ├── hypothesis/              # Experiment definitions
│   └── results/                 # Measured outcomes
│
├── research/                    # Research methodology and data
│   ├── data/                    # Research datasets
│   └── methodology/             # DMMF, DSRM documentation
│
├── papers/                      # Scientific output
│   ├── human-ai-collaboration/  # Main paper
│   └── templates/               # Paper templates
│
├── governance/                  # Lab governance
│   └── constitution.md          # Rules, standards, tech stack
│
├── docs/                        # Documentation
│   ├── architecture/            # Architectural decisions
│   ├── books/                   # Reference books
│   ├── personal/                # Personal materials
│   └── research/                # Research papers (PDFs)
│
├── tests/                       # Test suite (pytest)
│
├── config/                      # Configuration files
│
├── mcp_server.py                # MCP Server entry point
├── Dockerfile                   # Container definition
└── docker-compose.yml           # Container orchestration
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

### 2. Artifacts (`artifacts/`)

Produced resources including:
- **Agents** - Brazilian AI personas (Santos Dumont, Machado de Assis, etc.)
- **Prompts** - Technical skills and templates
- **Workflows** - Orchestrated multi-step processes

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

## Quick Start

### Environment Setup

```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Running Tests

```bash
pytest tests/ -v
```

### Running the MCP Server

```bash
# Local mode
python mcp_server.py

# Docker mode
docker-compose up
```

### Running the Pipeline

```bash
python -m src.pipeline.integration_pipeline --full
```

---

## Governance

See `governance/constitution.md` for:
- 4D Framework (Delegation, Description, Discernment, Diligence)
- Tech stack requirements
- Quality standards
- Agent responsibilities

---

## Versioning

### Semantic Versioning for Prompts

- **MAJOR** (X.0.0) - Fundamental life/context change
- **MINOR** (0.X.0) - New skill, significant capability
- **PATCH** (0.0.X) - Tweaks, calibration updates

### Current Version: 1.0.0

- Repository structure complete
- Personal meta-skill documented
- Evidence collection framework operational
- MCP Server deployed

---

## Roadmap

### Phase 1: Foundation
- [x] Repository structure
- [x] Personal meta-skill (`anderson-skill`)
- [x] Governance framework
- [x] MCP Server implementation

### Phase 2: Evidence Base
- [x] Metrics collection hooks
- [x] Pattern documentation
- [ ] Antipattern library expansion
- [ ] GitHub history analysis

### Phase 3: Experimentation
- [x] A/B testing framework
- [x] Metrics collection
- [ ] Hypothesis-driven improvements
- [ ] Automated calibration suggestions

### Phase 4: Automation
- [ ] CI/CD for prompt validation
- [ ] Quality metrics dashboard
- [ ] Cross-project pattern detection

---

## Principles

1. **Evidence Over Intuition** - Decisions traceable to observed outcomes
2. **Composition Over Monoliths** - Small, focused modules that combine
3. **Evolution Over Perfection** - Living documents that improve through iteration
4. **Transparency Over Magic** - Document WHY prompts work, not just WHAT
5. **Personal Over Generic** - Optimized for one human-AI partnership

---

## License

**Proprietary - All Rights Reserved**

This repository contains personal context, communication preferences, and proprietary prompt engineering strategies. Not open source.

For inquiries: andersonhs27@gmail.com

---

## Author

**Anderson Henrique da Silva**
- Location: Minas Gerais, Brasil
- Background: Philosophy -> Computer Science
- Focus: AI/ML Engineering, Multi-Agent Systems, AI Safety

---

*Last Updated: 2025-12-31*

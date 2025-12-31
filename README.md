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
├── CLAUDE.md                    # Entry point for AI assistants
├── README.md                    # This file
│
├── src/                         # Python source code
│   ├── core/                    # Core modules
│   │   ├── metrics/             # Metrics collection
│   │   ├── calibration/         # Dashboard and auto-calibration
│   │   ├── pipeline/            # Component orchestration
│   │   └── versioning/          # Version management
│   ├── analysis/                # Data analysis scripts
│   ├── experiments/             # A/B testing framework
│   ├── import/                  # Data importers
│   └── mcp/                     # MCP Server
│
├── data/                        # All data files
│   ├── raw/                     # Raw data
│   ├── processed/               # Processed data
│   └── metrics/                 # Collected metrics
│       ├── data/                # Interaction data (JSON)
│       ├── sessions/            # Session summaries
│       └── reports/             # Generated reports
│
├── research/                    # Research & Evidence
│   ├── methodology/             # DMMF, DSRM docs
│   ├── experiments/             # Hypotheses and results
│   │   ├── hypotheses/
│   │   └── results/
│   ├── evidence/                # Patterns and models
│   │   ├── patterns/
│   │   ├── antipatterns/
│   │   └── models/
│   └── literature.md            # External references (links)
│
├── artifacts/                   # Produced artifacts
│   ├── agents/                  # Brazilian AI personas
│   ├── prompts/                 # Prompt templates
│   │   ├── technical/           # Technical skills
│   │   └── legacy/              # Legacy prompts
│   ├── skills/                  # Claude Code skills
│   └── workflows/               # Orchestrated processes
│
├── personal/                    # Personal context (gitignored)
│   ├── SKILL.md                 # Entry point
│   ├── identity.md              # Background, values
│   ├── communication.md         # Style preferences
│   ├── contexts/                # Situational modes
│   ├── calibration/             # Good/bad interactions
│   └── goals.md                 # Current objectives
│
├── publications/                # Scientific output
│   ├── papers/                  # Research papers
│   ├── presentations/           # Talks, slides
│   └── templates/               # Paper templates
│
├── docs/                        # Documentation
│   ├── architecture/            # ADRs
│   ├── guides/                  # How-tos
│   └── references/              # PDFs, books
│
├── governance/                  # Lab governance
│   └── constitution.md          # Rules, standards
│
├── tests/                       # Test suite (pytest)
│
├── deploy/                      # Infrastructure
│   ├── Dockerfile
│   └── docker-compose.yml
│
└── config/                      # Configuration files
```

---

## Core Concepts

### 1. Personal Context (`personal/`)

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

### 3. Evidence Base (`research/evidence/`)

Empirical foundation built from:
- **GitHub History** - Commit patterns, PR discussions, code reviews
- **Project Analysis** - What worked in real projects
- **Interaction Logs** - Effective vs ineffective AI conversations
- **Metrics** - Response quality, iteration counts, time-to-solution

### 4. Experiments (`research/experiments/`)

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
python src/mcp/server.py

# Docker mode
cd deploy && docker-compose up
```

### Running the Pipeline

```bash
python -m src.core.pipeline.integration_pipeline --full
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
- [x] Personal meta-skill (`personal/`)
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

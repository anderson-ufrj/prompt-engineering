# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Prompt Engineering Lab** - a personal system for human-AI collaboration based on the Developer Mental Model Framework (DMMF). It implements a scientific approach to prompt engineering with evidence-based evolution and modular composition.

**Scientific Foundation:** DMMF research (Silva, 2025) - 40 repositories, 2,799 commits, mixed-methods approach.

## Architecture

```
prompt-engineering/
├── anderson-skill/          # Personal meta-skill (WHO + HOW to communicate)
│   ├── SKILL.md             # Entry point - load first for personal context
│   ├── core/                # Stable: identity, values, communication style
│   ├── dynamic/             # Volatile: goals, career status (update frequently)
│   ├── contexts/            # Situational modes: debug, interview, brainstorm
│   └── interactions/        # Calibration examples (good/bad patterns)
│
├── skills/                  # Technical skills library (WHAT to do)
│   ├── cognitive-workflows/ # Multi-LLM patterns (chain, parallel, route, etc.)
│   └── [skill-name]/        # Each skill has SKILL.md + optional resources
│
├── evidence/                # Empirical foundation
│   ├── patterns/            # Effective patterns extracted from research
│   ├── antipatterns/        # Patterns to avoid
│   ├── sources/             # Raw data (anthropic-cookbook, anthropic-courses)
│   └── metrics/             # Quantitative measurements
│
├── prompts/                 # Legacy prompts (migration in progress)
└── experiments/             # A/B testing framework for prompt improvements
```

## Core Concepts

### DMMF Dimensions (Cognitive Profile)
- **Cognitive:** Hierarchical structures, clear boundaries, modular thinking
- **Affective:** Quality as non-negotiable, tests = anxiety management
- **Conative:** Technology as civic tool, ethics and social impact
- **Reflective:** Continuous iteration, 41.9% refactor-related commits

### Skill System
Skills follow the Agent Skills Spec (YAML frontmatter + Markdown):
```yaml
---
name: skill-name
description: |
  When to use this skill
---
# Skill instructions here
```

### Composition Strategy
```
anderson-skill (personal context) + technical-skill (task-specific) = optimal interaction
```

## Working with This Repository

### Reading Context
1. **Always load `anderson-skill/SKILL.md` first** for communication preferences
2. **Check `evidence/patterns/`** for documented effective approaches
3. **Load situational context** from `anderson-skill/contexts/` based on task type

### Creating Skills
- Place in `skills/[skill-name]/SKILL.md`
- Follow Agent Skills Spec format
- Include clear "When to use" section in description

### Documentation
All documentation goes in `docs/` organized by category - never create docs at project root.

## Key Patterns

### Cognitive Workflows (from Anthropic research)
| Pattern | Use Case |
|---------|----------|
| Chain | Sequential transformations |
| Parallel | Multiple perspectives needed |
| Route | Input determines specialized handling |
| Orchestrator-Workers | Complex tasks with dynamic subtasks |
| Evaluator-Optimizer | Quality-critical iterative refinement |

### DMMF-Informed Interaction
- Present information hierarchically (matches cognitive style)
- Never skip tests or dismiss quality concerns
- Support iterative refinement (expect multiple passes)
- Connect technical decisions to broader impact

## Commit Guidelines

**Format:** `<type>(scope): summary`

Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`

**Language:** English, technical, objective

**Rules:**
- Summary limited to 60 characters
- Include extended description for significant changes
- No AI/tool mentions in commit messages

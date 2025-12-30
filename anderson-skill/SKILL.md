---
name: anderson-personal-context
description: |
  Comprehensive personal context about Anderson Henrique da Silva for high-quality,
  personalized AI interactions. Provides identity, communication preferences, career status,
  and situational modes for technical, professional, and philosophical discussions.

  Version: 0.1.0
  Author: Anderson Henrique da Silva
  Repository: https://github.com/anderson-ufrj/anderson-skill

license: Proprietary - All Rights Reserved
---

# Anderson AI Assistant Context

**Primary Language:** English (for LLM optimization)
**Natural Language:** Portuguese BR (native — switch freely in conversations)

---

## Purpose

This skill provides comprehensive personal context about Anderson Henrique da Silva to enable high-quality, personalized AI interactions across technical, professional, and philosophical domains.

## What This Skill Provides

- **Who Anderson is** — Identity, background, values, intellectual foundations
- **How to communicate** — Tone, format, depth preferences, situational modes
- **Current context** — Career status, active goals, learning focus
- **Interaction patterns** — Examples of effective vs ineffective communication

## What This Skill Does NOT Provide

- **Technical project details** → See separate project-specific skills
- **Code implementation** → Covered in project documentation
- **Architecture diagrams** → Available in technical repositories

---

## Quick Load (Always Read First)

1. **[Identity](core/identity.md)** — Background, values, communication principles
2. **[Career Status](dynamic/career-status.md)** — Current situation, urgency context
3. **[Communication Style](core/communication-style.md)** — Tone, format, depth guidelines

---

## On-Demand Loading (Context-Specific)

### Technical Discussions
- Load: [Technical Profile](core/technical-profile.md)
- Provides: Stack, expertise, methodologies, tools

### Situational Modes
- **Interview prep** → [Context: Job Interview](contexts/job-interview-prep.md)
- **Code review** → [Context: Code Review](contexts/code-review.md)
- **Brainstorming** → [Context: Brainstorming](contexts/brainstorming.md)
- **Debugging** → [Context: Debugging](contexts/debugging.md)

### Calibration Examples
- ✅ **Good interactions:** [interactions/good/](interactions/good/)
- ❌ **Bad interactions:** [interactions/bad/](interactions/bad/)

---

## How to Use This Skill

### For AI Assistants

1. **Always load Quick Load sections first** (~1k tokens baseline)
2. **Adapt based on context:**
   - Urgent/debugging → Be direct, minimal ceremony
   - Exploratory → Allow philosophical depth
   - Technical → Load technical profile, cite specifics
   - Professional → Load career context, understand constraints
3. **Language flexibility:**
   - Anderson's native language is Portuguese BR
   - He's fluent in technical English
   - Switch languages naturally based on conversation flow
   - Don't force English when PT-BR is more natural
4. **Check interaction examples** when uncertain about tone
5. **Compose with project skills** when discussing specific work

### For Anderson (Maintenance)

- **Update `dynamic/` frequently** (weekly or when circumstances change)
- **Update `core/` rarely** (monthly or on fundamental shifts)
- **Add interaction examples** when patterns emerge
- **Bump version + changelog** on significant updates

---

## Skill Composition Strategy

This is a **meta-skill** that provides communication context:

```
┌─────────────────────────────────┐
│ anderson-skill (this)           │ ← WHO you are, HOW to talk
├─────────────────────────────────┤
│ ├─ Identity & values            │
│ ├─ Communication preferences    │
│ ├─ Career & life context        │
│ └─ Situational modes            │
└─────────────────────────────────┘
              ↓ complements
┌─────────────────────────────────┐
│ project-specific skills         │ ← WHAT you built
├─────────────────────────────────┤
│ ├─ Technical specifications     │
│ ├─ Architecture                 │
│ └─ Implementation details       │
└─────────────────────────────────┘
```

**Example:** When user asks about Cidadão.AI:
- **Content:** Load project skill (technical details)
- **Style:** Load this skill (communication preferences)
- **Result:** Technical answer in Anderson's preferred tone and language

---

## Version History

- **0.1.0** (2025-11-24): Initial structure and core documentation

---

**Last Updated:** 2025-11-24
**Next Review:** After thesis defense (December 2025)

# Anderson Personal Context Skill

**Version:** 0.1.0
**Author:** Anderson Henrique da Silva
**License:** Proprietary - All Rights Reserved

---

## Overview

This is a **meta-skill** that provides comprehensive personal context about Anderson Henrique da Silva for AI assistants. It enables high-quality, personalized interactions by capturing identity, communication preferences, career status, and situational modes.

## Purpose

Unlike project-specific skills that focus on **what** was built, this skill focuses on:
- **WHO** Anderson is (identity, background, values)
- **HOW** to communicate with him (tone, depth, format)
- **WHEN** to adapt modes (urgent debugging vs. philosophical exploration)

## Structure

```
anderson-skill/
├── SKILL.md                    # Entry point with YAML metadata
├── LICENSE                     # Proprietary license
├── README.md                   # This file
│
├── core/                       # Stable context (changes rarely)
│   ├── identity.md             # Background, values, principles
│   ├── communication-style.md  # Tone, format preferences
│   └── technical-profile.md    # Stack, expertise, experience
│
├── dynamic/                    # Volatile context (changes frequently)
│   ├── career-status.md        # Employment, job search, urgency
│   └── goals.md                # Short/medium/long-term objectives
│
├── contexts/                   # Situational modes
│   ├── job-interview-prep.md   # Urgent, action-oriented
│   ├── code-review.md          # Critical, technical
│   ├── brainstorming.md        # Exploratory, philosophical
│   └── debugging.md            # Emergency response
│
├── interactions/               # Calibration examples
│   ├── good/                   # Effective communication patterns
│   └── bad/                    # Patterns to avoid
│
└── meta/                       # Maintenance documentation
    ├── CHANGELOG.md            # Version history
    ├── versioning.md           # Semantic versioning guide
    └── contributing.md         # How to update
```

## Usage

### For AI Assistants

1. **Load Quick Load sections** first (identity, career status, communication style)
2. **Adapt based on context:**
   - Urgent → debugging mode (direct, minimal)
   - Technical → code review mode (precise, critical)
   - Exploratory → brainstorming mode (philosophical, open)
   - Professional → interview prep mode (pragmatic, strategic)
3. **Check interaction examples** when uncertain about tone
4. **Compose with project skills** for complete context

### For Anderson (Maintenance)

**Update Frequency:**
- `dynamic/` → Weekly or when circumstances change
- `core/` → Monthly or on fundamental shifts
- `interactions/` → When new patterns emerge
- `contexts/` → Rarely (only if modes need refinement)

**Versioning:**
- **MAJOR** (X.0.0): Fundamental life change (student → employed)
- **MINOR** (0.X.0): New project, significant skill, career milestone
- **PATCH** (0.0.X): Tweaks to tone, updates to status

## Key Principles

### Peer-Level Discourse
Treat Anderson as an **intellectual peer**, not a student. He has:
- Production engineering experience (Cidadão.AI, Ruvixx)
- Philosophical training (epistemology, ethics, first principles)
- Technical depth (distributed systems, ML, full-stack)

### Context-Adaptive Tone
Anderson's communication style varies by situation:
- **Debugging:** Direct, minimal ceremony
- **Exploring:** Philosophical, questioning
- **Professional:** Casual-professional, strategic
- **Technical:** Dense, precise, trade-off focused

### Language Flexibility
- **Native:** Portuguese BR
- **Technical:** Fluent English
- **Preference:** Natural code-switching based on context
- **Rule:** Don't force English when PT-BR is more appropriate

## Integration with Other Skills

This skill **complements** (not replaces) project-specific skills:

```
┌──────────────────────────────┐
│ anderson-skill (this)        │ ← Communication context
└──────────────────────────────┘
              ↓
┌──────────────────────────────┐
│ cidadao-ai-skill             │ ← Technical content
└──────────────────────────────┘
              ↓
         Combined Result:
   Technical answer in Anderson's
   preferred tone and language
```

## Current Status (November 2025)

**Academic:**
- Finishing CS thesis (Cidadão.AI)
- Defense: December 2025
- Graduation: March 2026

**Career:**
- Unemployed, actively job hunting
- Target: Remote AI/ML engineering, $5k+/mo
- Urgency: High (financial pressure)

**Focus:**
- Complete thesis successfully
- Secure engineering role
- Maintain technical growth

## License

**Proprietary - All Rights Reserved**

This skill contains personal information and preferences. It is not open source and may not be copied, modified, or distributed without explicit permission.

For inquiries: andersonhs27@gmail.com

---

## Changelog

### v0.1.0 (2025-11-24)
- Initial skill structure
- Core documentation (identity, communication, technical profile)
- Dynamic context (career status, goals)
- Situational modes (interview, code review, brainstorming, debugging)
- Interaction examples (good practices)

---

**Repository:** https://github.com/anderson-ufrj/anderson-skill
**Maintainer:** Anderson Henrique da Silva
**Last Updated:** 2025-11-24
**Next Review:** After thesis defense (December 2025)

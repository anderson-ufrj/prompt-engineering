# Documentation & Reference Materials

This folder contains reference materials that inform the prompt engineering system.

---

## Structure

```
docs/
├── DSRM.pdf                                          # Design Science methodology
├── Design_Science_in_Information_Systems_Research.pdf # DS guidelines
├── books/          # Prompt engineering literature
├── research/       # Academic papers and articles
└── personal/       # CV, portfolio materials
```

---

## Contents

### Root (Methodological Foundations)
| File | Description |
|------|-------------|
| `DSRM.pdf` | Design Science Research Methodology (Peffers et al., 2008) - 6-step process model |
| `Design_Science_in_Information_Systems_Research.pdf` | Design Science in IS (Hevner et al., 2004) - 7 guidelines for DS research |

### books/
| File | Description |
|------|-------------|
| `Prompt-Engineering-for-LLMs-OReilly-2024.pdf` | O'Reilly comprehensive guide to LLM prompting |
| `compact-guide-to-large-language-models-ptbr.pdf` | Portuguese guide to LLMs |

### research/
| File | Description |
|------|-------------|
| `From-Commits-to-Cognition-Anderson.pdf` | DMMF research paper (Silva, 2025) - Scientific foundation for this project |

### personal/
| File | Description |
|------|-------------|
| `EN-CV_ANDERSON_H.pdf` | English CV for professional context |

---

## Key References

### DMMF Paper (Foundation)
**"From Commits to Cognition: A Mixed-Methods Framework for Inferring Developer Mental Models from Repository Artifacts"**

This paper provides the scientific basis for the prompt engineering system:
- 4 cognitive dimensions (Cognitive, Affective, Conative, Reflective)
- Empirical data from 40 repositories, 2,799 commits
- Mixed-methods approach (MSR + Thematic Analysis + Autoethnography)

Replication package: https://github.com/anderson-ufrj/dmmf_mental-model

### DSRM Papers (Methodological Foundation)
**"A Design Science Research Methodology for Information Systems Research"** (Peffers et al., 2008)

Provides the rigorous methodology for artifact creation:
- 6-step process: Problem → Objectives → Design → Demonstration → Evaluation → Communication
- Multiple entry points (problem-centered, objective-centered, design-centered, client-initiated)
- Iterative refinement loop

**"Design Science in Information Systems Research"** (Hevner et al., 2004)

Foundational paper with 7 guidelines for Design Science:
1. Design as artifact
2. Problem relevance
3. Design evaluation
4. Research contributions
5. Research rigor
6. Design as search process
7. Communication of research

---

## Adding New Materials

When adding new reference materials:
1. Place in appropriate subfolder
2. Update this README with description
3. If research-relevant, extract key insights to `evidence/patterns/`

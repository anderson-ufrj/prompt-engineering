# Documentation & Reference Materials

This folder contains reference materials that inform the prompt engineering system.

---

## Structure

```
docs/
├── books/          # Prompt engineering literature
├── research/       # Academic papers and articles
└── personal/       # CV, portfolio materials
```

---

## Contents

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

---

## Adding New Materials

When adding new reference materials:
1. Place in appropriate subfolder
2. Update this README with description
3. If research-relevant, extract key insights to `evidence/patterns/`

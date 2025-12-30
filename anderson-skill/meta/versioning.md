# Versioning Guide

This skill follows [Semantic Versioning 2.0.0](https://semver.org/) adapted for personal context management.

---

## Format: MAJOR.MINOR.PATCH

### MAJOR Version (X.0.0)

**When to increment:**
- Fundamental life/career transition
- Major identity shift that affects all interactions
- Breaking changes to how AI should interact with you

**Examples:**
- Student → Employed professional
- Single → Married/partnered (if affects availability/priorities)
- Brazil → International relocation
- Individual contributor → Manager/founder

**Impact:**
- All `core/` files likely need updates
- Situational modes may need complete revision
- Communication preferences may shift significantly

**Process:**
```bash
# Review ALL documentation
git checkout -b major-update-v2.0.0
# Update core/, dynamic/, contexts/
# Test with AI assistant
git commit -m "feat!: major career transition to employed professional

BREAKING CHANGE: Identity shifted from student to employed engineer.
Updated all communication modes, career status, and goals."
git tag v2.0.0
```

---

### MINOR Version (0.X.0)

**When to increment:**
- Significant milestone achieved
- New major project or skill acquired
- Important life event (graduation, MSc enrollment)
- Speaking engagement or publication

**Examples:**
- Thesis successfully defended
- Started new job (not just any job, but first employment)
- Completed major certification (MSc, not a Coursera course)
- Published research paper or major technical article
- Added new significant skill to repertoire

**Impact:**
- `dynamic/` files updated
- Possibly one new context mode
- Goals section revised
- Technical profile expanded

**Process:**
```bash
git checkout -b minor-update-v0.2.0
# Update relevant sections
git commit -m "feat: thesis defended successfully

- Updated career-status.md with post-defense context
- Revised goals for post-graduation phase
- Added context template for MSc enrollment"
git tag v0.2.0
```

---

### PATCH Version (0.0.X)

**When to increment:**
- Weekly/bi-weekly status updates
- Tweaks to communication style
- Minor corrections or clarifications
- Addition of interaction examples
- Goal progress updates

**Examples:**
- Job application status update
- Learning focus shifted to new technology
- Discovered new communication pattern
- Fixed typo or clarified ambiguous section
- Added interaction example

**Impact:**
- Minimal, localized changes
- Usually only `dynamic/` or `interactions/`
- No architectural changes to skill

**Process:**
```bash
# Quick update, no branch needed
git add dynamic/career-status.md
git commit -m "chore: update job search status

- Added 3 new applications
- Interview scheduled with Acme Corp"
git tag v0.0.5
```

---

## Version Decision Tree

```
Is this a fundamental identity shift?
├─ YES → MAJOR (X.0.0)
└─ NO
   ├─ Is this a significant milestone?
   │  ├─ YES → MINOR (0.X.0)
   │  └─ NO
   │     └─ Is this a regular update?
   │        └─ YES → PATCH (0.0.X)
```

---

## Examples by Category

### Career Changes

| Event | Version Impact | Rationale |
|-------|---------------|-----------|
| Job offer accepted | MAJOR (2.0.0) | Fundamental shift: student → employed |
| Promotion at existing job | MINOR (2.1.0) | Significant but not identity-changing |
| Interview scheduled | PATCH (2.1.1) | Regular status update |
| Job application submitted | PATCH (2.1.2) | Regular status update |

### Academic Changes

| Event | Version Impact | Rationale |
|-------|---------------|-----------|
| Thesis defended | MINOR (0.2.0) | Major milestone |
| Graduated | MINOR (0.3.0) | Major milestone |
| MSc enrolled | MINOR (0.4.0) | Significant new phase |
| Course completed | PATCH (0.4.1) | Progress update |

### Technical Skills

| Event | Version Impact | Rationale |
|-------|---------------|-----------|
| Mastered new tech stack | MINOR (0.5.0) | Significant capability expansion |
| Completed major project | MINOR (0.6.0) | Significant achievement |
| Learned new library | PATCH (0.6.1) | Incremental skill |
| Fixed code in old project | PATCH (0.6.2) | Maintenance |

### Personal Context

| Event | Version Impact | Rationale |
|-------|---------------|-----------|
| Relocated internationally | MAJOR (3.0.0) | Fundamental context shift |
| Changed career focus | MAJOR (4.0.0) | Identity-level change |
| New communication preference | PATCH (4.0.1) | Style tweak |
| Added interaction example | PATCH (4.0.2) | Documentation improvement |

---

## Git Workflow

### For MAJOR and MINOR versions:

```bash
# 1. Create feature branch
git checkout -b release-v0.2.0

# 2. Make changes
# Edit files as needed

# 3. Update CHANGELOG.md
# Add entry for new version

# 4. Update version in SKILL.md
# Change version: 0.2.0

# 5. Commit with conventional commit message
git commit -m "feat: thesis defended successfully"

# 6. Tag the release
git tag -a v0.2.0 -m "Release v0.2.0: Thesis defense milestone"

# 7. Push
git push origin main --tags
```

### For PATCH versions:

```bash
# Direct commit to main (no branch needed)
git add dynamic/career-status.md
git commit -m "chore: update job search status"
git tag v0.0.5
git push origin main --tags
```

---

## When to Review Versioning

- Before thesis defense (Nov/Dec 2025)
- After securing employment (target: Feb 2026)
- Every 6 months during employment
- When major life event occurs

---

## Commit Message Convention

Follow [Conventional Commits](https://www.conventionalcommits.org/):

**Format:** `<type>(<scope>): <description>`

**Types:**
- `feat`: New feature or significant addition
- `fix`: Bug fix or correction
- `docs`: Documentation changes
- `chore`: Routine updates (status, goals)
- `refactor`: Restructuring without changing meaning

**Examples:**
```bash
feat(career): add MSc cybersecurity enrollment
fix(identity): correct graduation date to March 2026
docs(contexts): improve interview prep template
chore(dynamic): update weekly job search status
refactor(core): reorganize technical profile structure
```

---

## Version History Reference

### Current: v0.1.0 (2025-11-24)
- Initial skill creation
- Core, dynamic, contexts, interactions established

### Upcoming: v0.2.0 (Dec 2025)
- Post-thesis defense update
- Career status shift to "defended, awaiting graduation"

### Future: v1.0.0 (Q1 2026)
- Employment secured
- Major identity shift: student → professional

---

**Maintainer:** Anderson Henrique da Silva
**Last Updated:** 2025-11-24

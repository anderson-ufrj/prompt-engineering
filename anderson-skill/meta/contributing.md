# Contributing Guide (Maintenance Workflow)

This document is for **Anderson** (the maintainer) to guide self-maintenance of this skill.

---

## Maintenance Philosophy

This skill is **living documentation** of your personal context. It should:
- **Evolve** as you change (career, skills, priorities)
- **Stay accurate** (outdated context is worse than no context)
- **Remain actionable** (AI assistants need clear guidance)

---

## Update Frequency

### Daily (if applicable)
- None (this isn't a journal)

### Weekly
- `dynamic/career-status.md` if job search active
- `dynamic/goals.md` if progress on short-term goals

### Monthly
- Review `core/communication-style.md` for new patterns
- Check `contexts/` for needed adjustments
- Audit interaction examples for recent conversations

### Quarterly
- Full review of `core/` files
- Update `technical-profile.md` with new skills
- Reassess goals alignment

### On Major Events
- **Immediately** after thesis defense
- **Immediately** after accepting job offer
- **Within a week** of starting new role
- **Within a week** of major project completion

---

## What to Update When

### When Job Status Changes

**Update:**
- `dynamic/career-status.md`
  - Employment status
  - Urgency level
  - Application pipeline status
  - Timeline adjustments

**Version:**
- PATCH for application/interview updates
- MINOR for offer acceptance (leads to MAJOR on start date)

**Example:**
```bash
git add dynamic/career-status.md
git commit -m "chore: add interview with Acme Corp on 2025-12-15"
git tag v0.1.1
```

---

### When Thesis Defense Happens

**Update:**
- `dynamic/career-status.md` (academic status → defended)
- `dynamic/goals.md` (mark thesis defense complete)
- `core/identity.md` (update timeline reference)
- `CHANGELOG.md` (document milestone)
- `SKILL.md` (bump version to 0.2.0)

**Version:** MINOR (0.2.0)

**Example:**
```bash
git checkout -b release-v0.2.0

# Edit files...

git add .
git commit -m "feat: thesis defended successfully

- Updated career status to post-defense phase
- Marked thesis completion in goals
- Adjusted identity timeline reference"

git tag -a v0.2.0 -m "Milestone: Thesis defense completed"
git push origin main --tags
```

---

### When Employment Secured

**Update:**
- `dynamic/career-status.md` (unemployed → employed)
- `dynamic/goals.md` (mark employment goal complete, add new goals)
- `core/identity.md` (update current situation)
- `contexts/job-interview-prep.md` (archive or mark as inactive)
- `CHANGELOG.md` (MAJOR version entry)
- `SKILL.md` (bump version to 1.0.0)

**Version:** MAJOR (1.0.0)

**Rationale:** Student → Professional is identity-level shift

**Example:**
```bash
git checkout -b major-release-v1.0.0

# Comprehensive updates...

git add .
git commit -m "feat!: career transition to employed AI engineer

BREAKING CHANGE: Identity shifted from student/job-seeking to employed professional.

- Updated career status: employed at [Company]
- Removed interview prep urgency
- Revised goals for professional phase
- Adjusted communication modes for employed context"

git tag -a v1.0.0 -m "Major Release: Employment secured"
git push origin main --tags
```

---

### When Learning New Skill/Technology

**Update:**
- `core/technical-profile.md` (add to stack)
- `dynamic/goals.md` (if was a learning goal)

**Version:**
- PATCH if incremental (new library)
- MINOR if significant (new tech stack mastery)

**Example (PATCH):**
```bash
git add core/technical-profile.md
git commit -m "chore: add Kubernetes to technical stack"
git tag v1.0.1
```

**Example (MINOR):**
```bash
git add core/technical-profile.md dynamic/goals.md
git commit -m "feat: mastered distributed tracing with Jaeger/OpenTelemetry"
git tag v1.1.0
```

---

### When Communication Pattern Discovered

**Update:**
- Add example to `interactions/good/` or `interactions/bad/`
- Optionally update `core/communication-style.md` if pattern is new

**Version:** PATCH

**Example:**
```bash
# Create new example file
cat > interactions/good/003-debugging-direct-fix.md << 'EOF'
# Good Interaction: Direct Debugging Fix
[Content...]
EOF

git add interactions/good/003-debugging-direct-fix.md
git commit -m "docs: add example of effective debugging response"
git tag v1.0.2
```

---

## Review Checklist

Use this before MAJOR or MINOR releases:

### Accuracy Check
- [ ] All dates are correct (defense, graduation, employment start)
- [ ] Career status reflects current reality
- [ ] Goals are up-to-date (mark completed, add new)
- [ ] Technical profile includes recent skills

### Consistency Check
- [ ] No contradictions between files
- [ ] Version numbers match across SKILL.md and CHANGELOG.md
- [ ] Links to other files work correctly

### Relevance Check
- [ ] Communication style still accurate?
- [ ] Contexts still apply? (e.g., interview prep after employment)
- [ ] Interaction examples still representative?

### Completeness Check
- [ ] CHANGELOG.md updated
- [ ] Version bumped in SKILL.md
- [ ] Git tag created
- [ ] README.md current status section updated

---

## When to Archive Content

### Job Interview Content
**When:** After securing stable employment (3+ months in)
**Action:** Move `contexts/job-interview-prep.md` to `archive/` or mark as inactive
**Rationale:** No longer urgent need, clutters active context

### Student-Specific Content
**When:** After graduation + 6 months employed
**Action:** Archive or condense student timeline in `core/identity.md`
**Rationale:** Professional identity supersedes student identity

### Outdated Goals
**When:** Goal abandoned or no longer relevant
**Action:** Mark with ~~strikethrough~~ in `dynamic/goals.md`, add explanation
**Rationale:** Track evolution, don't hide past priorities

---

## Git Workflow Summary

### Quick PATCH Update
```bash
# Edit file
git add <file>
git commit -m "chore: <description>"
git tag v0.X.Y
git push origin main --tags
```

### Planned MINOR Release
```bash
git checkout -b release-v0.X.0
# Edit multiple files
git commit -m "feat: <milestone>"
git tag -a v0.X.0 -m "Release description"
git push origin main --tags
```

### MAJOR Release (Rare)
```bash
git checkout -b major-release-vX.0.0
# Comprehensive updates
git commit -m "feat!: <breaking change>"
git tag -a vX.0.0 -m "Major release description"
git push origin main --tags
```

---

## Tools & Automation (Future)

### Potential Additions
- **Pre-commit hook:** Validate YAML in SKILL.md
- **Changelog generator:** Auto-generate from git commits
- **Link checker:** Ensure internal references work
- **Diff tool:** Compare skill versions over time

### Manual for Now
Until automation is needed, manual maintenance with discipline is sufficient.

---

## Emergency: Skill Out of Sync

If skill becomes significantly outdated:

1. **Stop using it** with AI assistants temporarily
2. **Block time** (2-3 hours) for comprehensive review
3. **Update all sections** following checklist above
4. **Bump to next MINOR** or MAJOR version
5. **Document gap** in CHANGELOG.md ("Updated after 6-month gap")
6. **Resume use** with AI assistants

**Prevention:** Set monthly calendar reminder for skill review.

---

## Questions to Ask During Review

1. **Identity:** Am I still the person described in `core/identity.md`?
2. **Career:** Does `dynamic/career-status.md` reflect my current situation?
3. **Goals:** Are my goals still aligned with reality?
4. **Communication:** Do I still want AI to interact with me this way?
5. **Contexts:** Are these modes still useful?
6. **Examples:** Do recent conversations match documented patterns?

If answer to any is "no" → update immediately.

---

## Final Note

**This skill is for you.** If maintenance becomes burdensome, simplify the structure. The goal is better AI interactions, not perfect documentation.

---

**Maintainer:** Anderson Henrique da Silva
**Last Updated:** 2025-11-24
**Next Review:** December 2025 (post-thesis defense)

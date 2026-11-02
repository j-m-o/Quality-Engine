# Public-release and sanitization checklist

## Confidentiality

- [ ] All work item keys, links and screenshots are synthetic or publication-approved.
- [ ] No organization names, customer names, internal teams, product identifiers or operational metrics from confidential systems remain.
- [ ] No internal domain, email, tokens, prompts, secrets, incident details or access-control configurations remain.
- [ ] Any tool screenshots show demo tenants or approved sample data.
- [ ] Any ownership and attribution statements reflect your desired public branding.

## Accuracy

- [ ] Scoring rubric identified as proposed, not empirically validated.
- [ ] No fabricated performance, ROI, defects avoided or coverage success claims.
- [ ] Missing or unavailable evidence is represented as Unknown.
- [ ] Schema fields, sample JSON, field mapping and comment labels agree.
- [ ] Jira automation and test provider compatibility checked in the target environment.

## Packaging

- [ ] Each skill contains `SKILL.md` with valid name and description frontmatter.
- [ ] Links and referenced assets resolve within the package.
- [ ] Package validation script passes.
- [ ] `python scripts/build.py` succeeds and `dist/` is rebuilt after any change under `skills/`.
- [ ] Integrations catalog has a current "Last checked" date and every row has an evidence level.
- [ ] Profile template defaults to read-only (`write_back.enabled: []`) and contains no credentials.
- [ ] Choose a license before public distribution.
- [ ] Add a repository URL, demo media and installation instructions once hosted.
- [ ] Consider adding tested integration adapters separately from the vendor-neutral core.

## Run local structural validation

```bash
python scripts/validate-package.py
```

Optionally scan for additional organization-specific names:

```bash
python scripts/validate-package.py --blocked-term "Private Organization Name" --blocked-term "internal.example"
```

---
*Quality Engine, created by **Jessica Mosley** | [LinkedIn](https://www.linkedin.com/in/jessmosley/) | [GitHub](https://github.com/j-m-o/)*

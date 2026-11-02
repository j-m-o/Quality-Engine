#!/usr/bin/env python3
"""Minimal structural and sample-data checks for this skills package.

Quality Engine, created by Jessica Mosley | LinkedIn: https://www.linkedin.com/in/jessmosley/ | GitHub: https://github.com/j-m-o/
"""
from pathlib import Path
import argparse
import json
import re
import sys

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--blocked-term', action='append', default=[], help='Additional case-insensitive forbidden text')
args = parser.parse_args()
errors = []
expected = {
    'quality-engine', 'coverage-review', 'qe-analysis', 'qe-planning-test-design',
    'security-review', 'accessibility-review', 'incident-intelligence',
    'metrics-intelligence'
}
actual = {p.name for p in (root / 'skills').iterdir() if p.is_dir()}
if actual != expected:
    errors.append(f'Skill folders do not match expected set: {sorted(actual ^ expected)}')
for name in sorted(expected):
    file = root / 'skills' / name / 'SKILL.md'
    if not file.exists():
        errors.append(f'Missing: {file}')
        continue
    body = file.read_text(encoding='utf-8')
    matched = re.match(r'^---\n(.*?)\n---\n', body, re.S)
    if not matched:
        errors.append(f'Missing YAML frontmatter: {file}')
        continue
    frontmatter = matched.group(1)
    title = re.search(r'^name: (.+)$', frontmatter, re.M)
    description = re.search(r'^description: (.+)$', frontmatter, re.M)
    if not title or title.group(1).strip() != name:
        errors.append(f'Invalid skill name: {file}')
    if not description or not description.group(1).strip():
        errors.append(f'Missing description: {file}')
    if description and len(description.group(1)) > 1024:
        errors.append(f'Description too long: {file}')
    for link in re.findall(r'\]\(([^)#]+)(?:#[^)]+)?\)', body):
        if not link.startswith(('http:', 'https:')) and not (file.parent / link).exists():
            errors.append(f'Broken skill link in {file}: {link}')

# Quality Engine specifics: profile template, integrations catalog and referenced files.
try:
    import yaml
    profile = yaml.safe_load((root / 'skills/quality-engine/assets/profile-template.yaml').read_text(encoding='utf-8'))
    for key in ('version', 'tools', 'modules', 'windows', 'write_back'):
        if key not in profile:
            errors.append(f'Profile template missing key: {key}')
    if profile.get('write_back', {}).get('enabled') != []:
        errors.append('Profile template must default to read-only (write_back.enabled: [])')
except ImportError:
    print('Optional pyyaml unavailable; skipped profile template parsing.')
catalog = (root / 'skills/quality-engine/references/integrations-catalog.md').read_text(encoding='utf-8')
if not re.search(r'Last checked: [A-Z][a-z]+ \d{1,2}, \d{4}', catalog):
    errors.append('Integrations catalog is missing its "Last checked" date')
levels = {'read', 'found', 'community', 'own-use', 'unchecked', 'n/a'}
for row in catalog.splitlines():
    cells = [c.strip() for c in row.strip().strip('|').split('|')]
    if row.startswith('|') and len(cells) == 4 and cells[0] not in ('Tool', '---') and not set(cells[0]) <= set('-: '):
        tokens = {t.strip() for t in cells[2].split(',')}
        if not tokens <= levels:
            errors.append(f'Catalog row has unknown evidence level: {cells[0]} -> {cells[2]}')
qe_dir = root / 'skills/quality-engine'
for md in qe_dir.rglob('*.md'):
    for ref in re.findall(r'`((?:references|assets)/[A-Za-z0-9_./-]+)`', md.read_text(encoding='utf-8')):
        if '<' in ref or ref.startswith('references/specialists/') or ref == 'references/profile.yaml':
            continue
        if not (qe_dir / ref).exists() and not (root / 'skills/qe-analysis' / ref).exists() \
                and ref != 'assets/feature-quality-assessment.schema.json':
            errors.append(f'Quality Engine references a missing file: {md.relative_to(root)} -> {ref}')

assessment = json.loads((root / 'examples/sample-assessment.json').read_text(encoding='utf-8'))
json.loads((root / 'schemas/feature-quality-assessment.schema.json').read_text(encoding='utf-8'))
parts = assessment['readinessComponents']
if sum(parts.values()) != assessment['fields']['featureQualityReadinessScore']:
    errors.append('Example readiness dimension scores do not sum to total score')
try:
    import jsonschema
    schema = json.loads((root / 'schemas/feature-quality-assessment.schema.json').read_text(encoding='utf-8'))
    jsonschema.Draft202012Validator(schema).validate(assessment)
except ImportError:
    print('Optional jsonschema library unavailable; skipped formal JSON schema validation.')
except Exception as exc:
    errors.append(f'JSON schema validation failed: {exc}')

for item in root.rglob('*'):
    if item.suffix not in ('.md', '.txt', '.json', '.mmd', '.py') or not item.is_file():
        continue
    text = item.read_text(encoding='utf-8').casefold()
    for term in args.blocked_term:
        if term.casefold() in text:
            errors.append(f'Blocked term found in {item.relative_to(root)}: {term}')

if errors:
    print('FAILED')
    for problem in errors: print('-', problem)
    sys.exit(1)
print(f'PASS: {len(expected)} skill folders, frontmatter, referenced skill assets, sample score and JSON validated.')

#!/usr/bin/env python3
"""Build distributable artifacts from the skills/ folders (the single source of truth).

Quality Engine, created by Jessica Mosley | LinkedIn: https://www.linkedin.com/in/jessmosley/ | GitHub: https://github.com/j-m-o/

Outputs under dist/:
  quality-engine.skill      Self-contained install: orchestrator plus the seven specialists
                            bundled under references/specialists/.
  specialists/<name>.skill  Optional standalone installs of each specialist.
  agents/<name>.md          Agent definitions generated from the same skills.
"""
from pathlib import Path
import json
import re
import shutil
import sys
import zipfile

root = Path(__file__).resolve().parents[1]
dist = root / 'dist'
name = 'quality-engine'
specialists = [
    'coverage-review', 'qe-analysis', 'qe-planning-test-design',
    'security-review', 'accessibility-review', 'incident-intelligence',
    'metrics-intelligence',
]

# Specialist bodies move from skills/<n>/ to references/specialists/ in the bundle.
link_map = {
    '](references/scoring-rubric.md)': '](../scoring-rubric.md)',
    '](assets/assessment-template.md)': '](../../assets/assessment-template.md)',
    '](assets/test-plan-template.md)': '](../../assets/test-plan-template.md)',
}
FRONTMATTER = re.compile(r'^---\n(.*?)\n---\n', re.S)


def split(text):
    m = FRONTMATTER.match(text)
    if not m:
        raise ValueError('missing frontmatter')
    desc = re.search(r'^description: (.+)$', m.group(1), re.M).group(1).strip()
    return desc, text[m.end():].lstrip('\n')


def zip_dir(src: Path, archive: Path, arcname: str):
    archive.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as z:
        for f in sorted(src.rglob('*')):
            if f.is_file():
                z.write(f, Path(arcname) / f.relative_to(src))


if dist.exists():
    shutil.rmtree(dist)
stage = dist / '_stage' / name

# ---- 1. Self-contained quality-engine skill -------------------------------
shutil.copytree(root / 'skills' / name, stage)
(stage / 'references' / 'specialists').mkdir(parents=True, exist_ok=True)
for s in specialists:
    _, body = split((root / 'skills' / s / 'SKILL.md').read_text(encoding='utf-8'))
    for old, new in link_map.items():
        body = body.replace(old, new)
    (stage / 'references' / 'specialists' / f'{s}.md').write_text(body, encoding='utf-8')
shutil.copy(root / 'skills/qe-analysis/references/scoring-rubric.md', stage / 'references/scoring-rubric.md')
shutil.copy(root / 'skills/qe-analysis/assets/assessment-template.md', stage / 'assets/assessment-template.md')
shutil.copy(root / 'skills/qe-planning-test-design/assets/test-plan-template.md', stage / 'assets/test-plan-template.md')
shutil.copy(root / 'schemas/feature-quality-assessment.schema.json', stage / 'assets/feature-quality-assessment.schema.json')
shutil.copy(root / 'NOTICE.md', stage / 'NOTICE.md')

# ---- 2. Verify the bundle is internally consistent ------------------------
errors = []
for md in stage.rglob('*.md'):
    text = md.read_text(encoding='utf-8')
    for link in re.findall(r'\]\(([^)#]+)(?:#[^)]+)?\)', text):
        if not link.startswith(('http:', 'https:')) and not (md.parent / link).exists():
            errors.append(f'Broken link in {md.relative_to(stage)}: {link}')
    for ref in re.findall(r'`((?:references|assets)/[A-Za-z0-9_./-]+)`', text):
        if '<' in ref or ref == 'references/profile.yaml':  # user-created, optional
            continue
        if not (stage / ref).exists():
            errors.append(f'Missing file referenced in {md.relative_to(stage)}: {ref}')
router = (stage / 'SKILL.md').read_text(encoding='utf-8')
for s in specialists:
    if f'`{s}`' not in router:
        errors.append(f'Orchestrator does not mention specialist: {s}')
if errors:
    print('BUILD FAILED')
    for e in errors:
        print('-', e)
    sys.exit(1)

zip_dir(stage, dist / f'{name}.skill', name)

# ---- 3. Optional standalone specialists -----------------------------------
for s in specialists:
    zip_dir(root / 'skills' / s, dist / 'specialists' / f'{s}.skill', s)

# ---- 4. Agent definitions -------------------------------------------------
agents = dist / 'agents'
agents.mkdir(parents=True)


def strip_relative_links(text):
    return re.sub(r'\[([^\]]+)\]\((?!https?:)[^)]+\)', r'\1', text)


def agent_file(agent_name, desc, body, tools=None, preface=''):
    fm = ['---', f'name: {agent_name}', f'description: {json.dumps(desc)}']
    if tools:
        fm.append(f'tools: {tools}')
    fm.append('---')
    (agents / f'{agent_name}.md').write_text(
        '\n'.join(fm) + '\n\n' + preface + strip_relative_links(body), encoding='utf-8')


for s in specialists:
    desc, body = split((root / 'skills' / s / 'SKILL.md').read_text(encoding='utf-8'))
    preface = ('> You are a specialist agent called by the Quality Engine orchestrator. '
               'Work only from the evidence packet you are given. Do not query trackers, '
               'test platforms, telemetry or chat. If something is missing, say "not verified".\n\n')
    agent_file(s, desc, body, tools='Read, Grep, Glob', preface=preface)

desc, body = split((root / 'skills' / name / 'SKILL.md').read_text(encoding='utf-8'))
preface = ('> Agent mode: where this text says to invoke a specialist skill, delegate to the specialist '
           'agent of the same name if your host supports delegation. Otherwise follow that specialist\'s '
           'instructions yourself using the evidence packet. Grant this agent only the connectors the '
           'profile selects, and leave write tools out until a write-back is enabled.\n\n')
agent_file(name, desc, body, preface=preface)

shutil.rmtree(dist / '_stage')
print('Built:')
for f in sorted(dist.rglob('*')):
    if f.is_file():
        print(' ', f.relative_to(root))

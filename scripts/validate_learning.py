#!/usr/bin/env python3
"""Valida destinos locais Markdown/HTML, SVG e presença dos módulos. Sem rede."""
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlsplit
ROOT=Path(__file__).resolve().parents[1]
errors=[]
for file in ROOT.rglob('*.md'):
    text=file.read_text(encoding='utf-8')
    text=re.sub(r'```.*?```','',text,flags=re.S)
    targets=re.findall(r'!?\[[^\]]*\]\(([^\s)]+)(?:[^)]*)\)',text)
    targets+=re.findall(r'(?:src|href)="([^"]+)"',text)
    for target in targets:
        u=urlsplit(target)
        if u.scheme or u.netloc or not u.path:
            continue
        path=(file.parent/unquote(u.path)).resolve()
        if not path.exists():
            errors.append(f'{file.relative_to(ROOT)}: destino ausente {target}')
for svg in (ROOT/'assets').glob('*.svg'):
    try:
        ET.parse(svg)
    except ET.ParseError as error:
        errors.append(f'{svg.name}: {error}')
modules=sorted((ROOT/'modules').glob('[0-9][0-9]-*.md'))
if len(modules)!=12:
    errors.append(f'Esperados 12 módulos; encontrados {len(modules)}')
for file in modules:
    text=file.read_text(encoding='utf-8')
    for marker in ('## Objetivo','## Prática guiada','## Entrega e aprovação'):
        if marker not in text:
            errors.append(f'{file.name}: seção ausente {marker}')
if errors:
    print('\n'.join(errors),file=sys.stderr)
    sys.exit(1)
print('OK: destinos locais, XML SVG e 12 módulos. Âncoras e URLs externas não verificadas.')

#!/usr/bin/env python3
"""Valida o esquema e a consistência do catálogo local; não faz requisições web."""
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "resources" / "catalog.json"
FIELDS = {"id", "title", "url", "category", "level", "kind", "language", "why", "origin"}
LEVELS = {"todos", "iniciante", "intermediario", "avancado"}


def validate():
    errors = []
    doc = json.loads(CATALOG.read_text(encoding="utf-8"))
    if not isinstance(doc.get("resources"), list) or not doc["resources"]:
        errors.append("O catálogo precisa de 'resources' como lista não vazia.")
        return errors, 0
    seen_ids = set()
    seen_urls = set()
    for idx, item in enumerate(doc["resources"], start=1):
        label = f"resources[{idx}]"
        if not isinstance(item, dict):
            errors.append(f"{label}: entrada não é objeto")
            continue
        missing = FIELDS - item.keys()
        if missing:
            errors.append(f"{label}: campos ausentes: {sorted(missing)}")
            continue
        if any(not isinstance(item[key], str) or not item[key].strip() for key in FIELDS):
            errors.append(f"{label}: campos devem ser strings não vazias")
            continue
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", item["id"]):
            errors.append(f"{label}: id inválido")
        if item["level"] not in LEVELS:
            errors.append(f"{label}: nível inválido")
        parsed = urlsplit(item["url"])
        if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
            errors.append(f"{label}: URL HTTPS pública e sem credenciais obrigatória")
        if item["id"] in seen_ids:
            errors.append(f"{label}: id duplicado")
        if item["url"].rstrip("/") in seen_urls:
            errors.append(f"{label}: URL duplicada")
        seen_ids.add(item["id"])
        seen_urls.add(item["url"].rstrip("/"))
    return errors, len(doc["resources"])


if __name__ == "__main__":
    problems, total = validate()
    if problems:
        print("\n".join("ERRO: " + item for item in problems), file=sys.stderr)
        sys.exit(1)
    print(f"Catálogo válido: {total} recursos; checagem estrutural concluída.")


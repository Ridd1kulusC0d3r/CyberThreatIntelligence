#!/usr/bin/env python3
"""Laboratório SQL offline. Python 3.10+ e SQLite 3.38+ (unixepoch)."""
import csv
import sqlite3
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def main():
    if sqlite3.sqlite_version_info < (3, 38, 0):
        raise SystemExit('Necessário SQLite >=3.38 para unixepoch().')
    with sqlite3.connect(':memory:') as db:
        db.execute('CREATE TABLE events(event_id INTEGER PRIMARY KEY,tenant TEXT,ts TEXT,account TEXT,src_ip TEXT,outcome TEXT)')
        with (ROOT/'datasets/auth-events.csv').open(encoding='utf-8', newline='') as handle:
            db.executemany('INSERT INTO events VALUES (?,?,?,?,?,?)', (tuple(r.values()) for r in csv.DictReader(handle)))
        query = (ROOT/'labs/auth-correlation.sql').read_text(encoding='utf-8')
        found = db.execute(query).fetchall()
        expected = [(4,'A','ana','192.0.2.10',3)]
        if found != expected:
            raise SystemExit(f'Falha: esperado {expected!r}; obtido {found!r}')
        # Contraprovas: uma falha exatamente no limite entra; fora do limite não entra.
        db.execute("UPDATE events SET ts='2026-01-01T09:58:00Z' WHERE event_id=1")
        if db.execute(query).fetchall() != expected:
            raise SystemExit('Falha no limite inclusivo de 300 segundos')
        db.execute("UPDATE events SET ts='2026-01-01T09:57:59Z' WHERE event_id=1")
        if db.execute(query).fetchall():
            raise SystemExit('Falha: incluiu evento fora da janela')
        print('OK: cenário positivo, controles negativos, isolamento de cliente e limite temporal.')
        print('Resultado original:', found)
        print('Padrão para investigação; não prova comprometimento.')
if __name__ == '__main__':
    main()

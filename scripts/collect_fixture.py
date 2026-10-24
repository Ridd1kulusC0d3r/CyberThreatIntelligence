#!/usr/bin/env python3
"""Coletor didático offline: versões por hash, rejeições e persistência atômica.
Não implementa API, autenticação, concorrência ou checkpoints de produção.
"""
import argparse
import hashlib
import json
import os
import tempfile
from datetime import datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
FIELDS=('source_id','id','observed_at','text')

def collect(source, output, fail_after=None):
    items=json.loads(source.read_text(encoding='utf-8'))
    if not isinstance(items,list):
        raise ValueError('A entrada deve ser uma lista')
    state=json.loads(output.read_text(encoding='utf-8')) if output.exists() else {'records':{},'rejected':{}}
    for index,item in enumerate(items,1):
        raw=json.dumps(item,ensure_ascii=False,sort_keys=True,separators=(',',':'))
        digest=hashlib.sha256(raw.encode()).hexdigest()
        try:
            if not isinstance(item,dict) or any(not isinstance(item.get(k),str) or not item[k].strip() for k in FIELDS):
                raise ValueError('Campos obrigatórios ausentes/inválidos')
            timestamp=datetime.fromisoformat(item['observed_at'].replace('Z','+00:00'))
            if timestamp.tzinfo is None:
                raise ValueError('Timestamp sem fuso')
            state['records'][digest]={'sha256':digest,'raw':item}
        except ValueError as error:
            state['rejected'][digest]={'raw':item,'reason':str(error)}
        if fail_after==index:
            raise RuntimeError('Interrupção simulada antes de persistir o lote')
    output.parent.mkdir(parents=True,exist_ok=True)
    tmp=None
    try:
        with tempfile.NamedTemporaryFile(mode='w',encoding='utf-8',dir=output.parent,delete=False) as f:
            tmp=Path(f.name)
            json.dump(state,f,ensure_ascii=False,indent=2,sort_keys=True)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp,output)
    finally:
        if tmp and tmp.exists():
            tmp.unlink()
    return state

def self_test():
    with tempfile.TemporaryDirectory() as directory:
        output=Path(directory)/'state.json'
        source=ROOT/'datasets/source-fixture.json'
        state=collect(source,output)
        assert len(state['records'])==2 and len(state['rejected'])==1
        before=output.read_bytes()
        collect(source,output)
        assert output.read_bytes()==before, 'Reprocessamento não idempotente'
        try:
            collect(source,output,fail_after=2)
        except RuntimeError:
            pass
        else:
            raise AssertionError('Falha não foi simulada')
        assert output.read_bytes()==before, 'Interrupção alterou estado persistido'
        collect(source,output)
        assert output.read_bytes()==before
    print('OK: duplicata, edição preservada, quarentena, idempotência e recuperação.')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--self-test',action='store_true')
    parser.add_argument('--output',type=Path,default=ROOT/'lab-output/state.json')
    args=parser.parse_args()
    if args.self_test:
        self_test()
    else:
        result=collect(ROOT/'datasets/source-fixture.json',args.output)
        print(f"{len(result['records'])} versões; {len(result['rejected'])} rejeições; saída: {args.output}")

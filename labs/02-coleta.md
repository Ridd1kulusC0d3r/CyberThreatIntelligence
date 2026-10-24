# Lab 02 / Coleta recuperável

[← Laboratórios](README.md) · **4 horas** · CTI M03–M04 / SOC S06

## Missão

Preservar edições, eliminar duplicatas exatas e tornar rejeições visíveis. O [fixture](../datasets/source-fixture.json) contém quatro entradas: original, duplicata, edição e registro inválido.

1. Leia o contrato em `scripts/collect_fixture.py` e preveja o resultado.
2. Execute `python3 scripts/collect_fixture.py --self-test`.
3. Execute `python3 scripts/collect_fixture.py` duas vezes; compare o estado em `lab-output/state.json`.
4. Explique por que existem duas versões válidas e uma rejeição.
5. Descreva como adaptar o desenho a paginação, credenciais e rate limit de uma API, sem implementar acesso real neste exercício.

## Falha e recuperação

O self-test interrompe a execução antes da persistência; o arquivo anterior permanece íntegro e o lote pode ser reprocessado. Não é um coletor de produção: não há concorrência, paginação, checkpoint remoto ou agendamento. Hash do registro apoia integridade e deduplicação, não autenticidade da fonte.

## Entrega

Contrato de dados, saída resumida, explicação da falha e runbook. Aprovação: declarar limites reais, preservar versões e explicar a quarentena. Não remover registros inválidos silenciosamente.

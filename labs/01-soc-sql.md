# Lab 01 / Autenticação: sinal não é veredito

[← Laboratórios](README.md) · **3–4 horas** · CTI M09 / SOC S03–S04

## Missão

Encontrar sucessos precedidos por pelo menos três falhas da mesma conta, IP e cliente nos cinco minutos anteriores. Trabalhar com [eventos sintéticos](../datasets/auth-events.csv). Pré-requisito: SELECT, JOIN, GROUP BY e timestamps UTC.

1. Leia os eventos sem executar a solução; escreva quais contas merecem revisão.
2. Crie consulta SQLite que respeite cliente e intervalo temporal.
3. Compare com [consulta de referência](auth-correlation.sql).
4. Execute `python3 scripts/run_soc_lab.py` na raiz.
5. Explique por que bia, caio, dani e eli não satisfazem a regra.
6. Solicite contexto de MFA, dispositivo, manutenção e inventário antes de concluir comprometimento.

## Resultado e contraprovas

O caso positivo é evento 4, cliente A, ana, com três falhas. Bia tem só uma; caio está fora da janela; dani mistura clientes; eli tem falhas posteriores. O runner também verifica os limites de 300 e 301 segundos.

## Mudança de cenário

Uma manutenção autorizada pode explicar ana. O padrão continua detectado, mas o julgamento do incidente pode mudar. Diferencie validade da consulta, precisão no corpus e interpretação de negócio.

## Entrega

Consulta comentada, resultado, duas hipóteses e [relatório de incidente](../templates/incidente.md). Aprovação: sem junção entre clientes, sem eventos posteriores e sem atribuição automática de ataque. A consulta é didática; não cobre password spraying distribuído nem todas as tentativas de força bruta.

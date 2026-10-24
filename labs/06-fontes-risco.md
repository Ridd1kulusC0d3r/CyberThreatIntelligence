# Lab 06 / Fontes, prioridade e risco

[← Laboratórios](README.md) · **4 horas** · CTI M02 / SOC S07

## Cenário sintético

F1 relata exploração de vulnerabilidade em produto X sem artefatos; F2 e F3 repetem F1. F4 apresenta relatório técnico independente. O inventário fictício contém X exposto em serviço crítico, Y interno com correção disponível e Z fora de suporte sem evidência de exploração. Não há CVEs reais neste exercício.

1. Avalie independência e credibilidade separadamente.
2. Defina PIR e coleta necessária para confirmar presença/versão de X.
3. Priorize X/Y/Z considerando exposição, impacto e incerteza.
4. Crie plano de teste e patches com janela, rollback e validação.
5. Registre exceção temporária caso o serviço crítico não possa ser interrompido.
6. Escreva nota executiva explicando o que se sabe e o que falta.

Aprovação: F1/F2/F3 não contam como três confirmações independentes; presença de produto não comprova vulnerabilidade; decisão de risco residual tem responsável e data de revisão. Usar [ficha de fonte](../templates/fontes.md) e [registro de risco](../templates/risco-patches.md).

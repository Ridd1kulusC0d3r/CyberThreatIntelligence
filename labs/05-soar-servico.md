# Lab 05 / Automação com falhas e decisão humana

[← Laboratórios](README.md) · **4 horas** · SOC S01/S06/S08

## Cenário

Um alerta de um cliente envolve servidor crítico. O enriquecimento retorna reputação suspeita, mas o inventário está indisponível. O playbook não pode assumir que o ativo é descartável ou que a reputação prova incidente.

## Exercício de mesa

1. Desenhe estados: recebido, validado, enriquecido, aguardando decisão, ação, verificação, encerrado/erro.
2. Defina responsável, permissões, escopo por cliente e chave de idempotência.
3. Simule timeout do enriquecimento, evento repetido e falha parcial da ação.
4. Exija decisão responsável antes de contenção que afete disponibilidade.
5. Defina compensação/rollback, handover e trilha de auditoria.
6. Faça revisão de 20 minutos com colega e registre dúvidas.

## Entrega e aprovação

Playbook documentado, [ficha do serviço](../templates/servico-soc.md) e três testes de mesa. Sem contexto suficiente, escalar com lacunas explícitas; não inventar sucesso de ação. Avaliar o desenho, não alegar integração SOAR implantada. Extensão: implementar apenas enriquecimento benigno em laboratório próprio.

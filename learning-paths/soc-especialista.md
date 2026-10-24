# Especialista em SOC / Operação, investigação e melhoria

[← Início](../README.md) · [CTI](cti-48-semanas.md) · [Normas e RFCs](../docs/09-normas-e-rfcs.md)

**24 semanas · 12 h/semana · 288 horas propostas.** Trilha complementar à CTI, com pré-requisitos de redes, Windows/Linux e scripting. Formação completa CTI + SOC: 864 horas sem equivalências. Não é certificação, promessa de contratação ou substituição de experiência em missão crítica.

O perfil foi derivado das competências de uma descrição de vaga fornecida pelo mantenedor. Local, empregador e alegações promocionais da vaga não são requisitos educacionais nem endosso do projeto.

## Matriz de competências e evidências

| Responsabilidade ou requisito | Estudo | Evidência exigida |
|---|---|---|
| Sustentar serviços em todo o ciclo de vida | S01 | Catálogo, aceite, operação, melhoria e saída do serviço |
| Blue Team em missão crítica | S01/S04 | Contenção proporcional, continuidade e recuperação validada |
| Investigação formal e relatório técnico | S04 | Escopo, linha do tempo, evidências, decisões e revisão |
| Análise de ameaças e benchmarking | S03/S08 | Caso de uso e comparação com dados equivalentes |
| Multiplicação de conhecimento | S08 | Workshop, feedback e artigo técnico |
| ATT&CK e D3FEND | S03 | Comportamento → técnica defensiva → telemetria → teste |
| Redes e RFCs citadas | S02 | Explicação de pacotes e aplicação contextual das RFCs |
| SIEM, SOAR e SQL | S03/S06 | Consulta testada, playbook com aprovação e tratamento de falhas |
| ISO 27001/27002 | S07 | Relação entre objetivo, controle e evidência operacional |
| ISO 31000/27005 | S07 | Registro de risco, tratamento, responsável e revisão |
| NIST SP 800-40 | S07 | Plano de patches com teste, exceção, rollback e validação |
| NIST SP 800-61 | S04 | Plano de resposta integrado à gestão de risco |
| Malware estático/dinâmico e MAR | S05 | Relatório com métodos, comportamento e limitações |
| Python/Bash/PowerShell | S06 | Automação com logs, erros e modo de simulação |
| Linux/Windows e Ansible | S02/S06 | Baseline de laboratório e evidência de idempotência |
| Inglês avançado | S08 e prática semanal | Leitura técnica, escrita e apresentação com perguntas |
| Comunicação e autogestão | S01/S08 | Priorização, handover, briefing e retrospectiva |

## S01 / Serviço SOC e missão crítica — semanas 1–3

**Estudar:** catálogo de serviços, onboarding de clientes, RACI, SLA/OLA, escopo de monitoração, inventário de ativos, separação de clientes, retenção, capacidade, escalonamento e encerramento de serviço. Não assumir que toda contenção automática é aceitável em ambiente crítico.

**Prática:** definir um serviço para uma organização fictícia, com 20 ativos e três fontes de logs. Na primeira semana, mapear proprietários e criticidade; na segunda, produzir critérios de aceite e handover; na terceira, simular indisponibilidade de uma fonte crítica.

**Entrega:** [ficha de serviço](../templates/servico-soc.md), matriz RACI e relatório de indisponibilidade.

**Aprovação:** outro analista explica cobertura e lacunas; os critérios de escalonamento incluem impacto, urgência, dono da decisão e alternativa de continuidade. Definir SLA de exercício, sem apresentá-lo como padrão universal.

## S02 / Redes, sistemas e telemetria — semanas 4–6

**Estudar:** TCP/UDP, DNS, ARP, FTP, endereçamento privado, roteamento e segmentação; logs Windows e Linux; sincronização temporal e perda de telemetria. A [matriz de RFCs](../docs/09-normas-e-rfcs.md) distingue referências essenciais, históricas e dependentes do ambiente.

**Prática:** interpretar captura de laboratório e montar linha do tempo de autenticação, resolução DNS e conexão. Comparar logs de dois hosts próprios; documentar campos, fuso e lacunas. Preparar baseline de coleta e verificar reinício de serviço.

**Entrega:** mapa de fontes de logs, dicionário de campos, hipótese de falha e plano de continuidade.

**Aprovação:** distinguir conexão falha de autenticação falha; explicar por que ausência de log não prova ausência de atividade. Não memorizar números de RFC sem entender o protocolo.

## S03 / SIEM, SQL e engenharia de detecção — semanas 7–9

**Estudar:** ingestão, parsing, normalização, correlação, janelas temporais, joins, cardinalidade e duplicação. Em ATT&CK, mapear comportamento observado; em D3FEND, justificar técnica defensiva e dependências. Não há garantia automática de cobertura por mapeamento.

**Prática:** executar o [lab SQL](../labs/01-soc-sql.md); traduzir a lógica para a linguagem do SIEM disponível, indicando diferenças semânticas. Projetar detecção com telemetria, testes positivos/negativos e critérios de ajuste.

**Entrega:** consulta, resultados esperados, caso de uso, mapeamento e registro de tuning.

**Aprovação:** não misturar clientes; respeitar janela temporal; explicar falsos positivos e o efeito de dados ausentes. Medir precisão somente em amostra rotulada e declarar tamanho e viés dessa amostra.

## S04 / Investigação e resposta formal — semanas 10–12

**Estudar:** [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final), escopo, severidade, evidências, preservação, cronologia, comunicação, contenção, erradicação, recuperação e lições aprendidas. A revisão 3 integra resposta à gestão de risco e ao CSF 2.0; não apresentar o ciclo da revisão 2 como se fosse a estrutura normativa atual.

**Prática:** investigar o caso sintético de autenticação; receber informação adicional de manutenção autorizada; revisar severidade. Propor contenção de endpoint crítico com alternativas e plano de retorno, sem executar em terceiros.

**Entrega:** [relatório de incidente](../templates/incidente.md) e handover verbal de cinco minutos.

**Aprovação:** cada decisão tem evidência, responsável e horário; recuperação exige validação; a investigação pode encerrar como atividade legítima se a evidência sustentar isso.

## S05 / Malware e MAR — semanas 13–15

**Estudar:** formatos, hashes, strings, imports, comportamento de processo, arquivos, persistência e rede. Distinguir indicador estático, inferência e observação dinâmica. MAR significa aqui **Malware Analysis Report**; confirmar o uso da sigla em cada organização.

**Prática:** realizar o [laboratório de MAR](../labs/04-malware-mar.md). Extensão dinâmica: ambiente isolado próprio, snapshots, rede controlada e telemetria, usando artefato benigno autorizado. Para malware real, exigir ambiente especializado e procedimento institucional; o repositório não distribui amostras.

**Entrega:** [MAR](../templates/mar.md), registro de ambiente, resultados positivos e negativos e hipóteses restantes.

**Aprovação:** não concluir comunicação C2 porque uma URL aparece em strings; não afirmar comportamento dinâmico sem log de execução. Registrar limitações de sandbox, duração e estímulos ausentes.

## S06 / SOAR, scripting e automação — semanas 16–18

**Estudar:** Python, Bash ou PowerShell; APIs, segredos, idempotência, permissões, retries, auditoria, dry-run e rollback. Ansible: inventário, módulos, variáveis, check mode e validação após mudança. Check mode não substitui teste real em ambiente de laboratório.

**Prática:** usar o coletor local como base; desenhar playbook de enriquecimento → decisão → ação aprovada → verificação. Simular timeout, execução duplicada e credencial expirada. Criar um playbook Ansible que aplique configuração benigna em uma VM própria e mostrar segunda execução sem alteração desnecessária.

**Entrega:** automação ou playbook de laboratório, runbook e [exercício SOAR](../labs/05-soar-servico.md).

**Aprovação:** nenhuma ação sensível depende só de score externo; falha parcial não gera sucesso silencioso; execução é auditável e escopo por cliente é preservado.

## S07 / Risco, controles e vulnerabilidades — semanas 19–21

**Estudar:** requisitos de SGSI na ISO/IEC 27001; controles na 27002; risco na ISO 31000/27005; planejamento de patches na NIST SP 800-40 Rev. 4. Patching é parte da gestão de vulnerabilidades, não seu sinônimo.

**Prática:** priorizar cinco vulnerabilidades fictícias por exposição, criticidade, exploração conhecida e controles existentes. Preparar janela, teste, rollback, exceção com validade e validação posterior. Relacionar o caso a objetivos de controle, sem declarar conformidade com base em uma única evidência.

**Entrega:** [registro de risco](../templates/risco-patches.md), plano de tratamento e mapa de evidências.

**Aprovação:** risco residual tem dono; exceções expiram; correção é verificada. As páginas públicas da ISO dão contexto, mas estudo detalhado de requisitos depende de acesso autorizado ao texto integral.

## S08 / Liderança técnica e comunicação — semanas 22–24

**Estudar:** benchmarking justo, documentação, apresentação técnica, revisão por pares, mentoring, priorização e gestão de mudanças.

**Prática:** comparar duas abordagens de detecção sobre o mesmo corpus; preparar workshop de 20 minutos e briefing de cinco minutos em inglês. Produzir nota técnica de 500 palavras em inglês, receber perguntas e revisar termos ambíguos. Essas tarefas evidenciam comunicação, mas não certificam fluência.

**Entrega:** benchmark, apresentação, plano de melhoria e feedback dos participantes.

**Aprovação:** comparação declara ambiente, versões, dados e limitações; melhorias têm responsável, prazo e medida de sucesso; estudante responde perguntas sem ocultar incertezas.

## Rotina e conclusão

Por semana: 2 h de leitura primária, 5 h de laboratório, 2 h de documentação, 2 h de revisão e 1 h de inglês técnico. Distribuir leitura de RFCs conforme S02 e consultar durante investigações.

Concluir com o [projeto integrado](../capstones/cti-soc.md) adaptado ao serviço SOC. Aplicar a [rubrica](../assessments/rubrica.md). Este currículo oferece exercícios guiados e dois laboratórios locais executáveis; SIEM real, Ansible e análise dinâmica são práticas a executar no ambiente do estudante, não integrações já implantadas por este repositório.

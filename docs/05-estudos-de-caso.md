# 05 · Laboratório de análise: três estudos de caso

> Os cenários A e B são inteiramente fictícios e não descrevem pessoas, organizações ou incidentes reais. O terceiro é um roteiro de leitura histórica, sem reprodução de código ofensivo.

[← Trilhas](04-trilhas.md) · [Relatórios →](06-relatorios.md)

## Caso A · Fornecedor falso e campanhas de engenharia social

**Organização fictícia:** Cooperativa Boreal. **PIR:** há evidências suficientes de ação coordenada contra os parceiros da cooperativa?  
**Dados simulados:** três comunicados públicos sobre tentativas de imitação de marca; períodos semelhantes; imagens e mensagens parecidas; nenhuma telemetria interna disponível.

**Hipóteses:**
- H1: um único grupo conduziu uma campanha em várias organizações.
- H2: atores distintos reutilizaram modelos acessíveis.
- H3: relatórios secundários reproduziram o mesmo episódio.

**Análise esperada:** registrar quais informações são independentes; separar similaridade superficial de infraestrutura comprovadamente compartilhada; indicar o que não se pode inferir.

**Produto:** nota com conclusão provisória, confiança moderada ou baixa devidamente justificada, e medidas defensivas de verificação de comunicações oficiais.

## Caso B · Geopolítica e alegações de atribuição

**Cenário fictício:** após uma crise diplomática, aparecem publicações acusando um país de conduzir intrusões contra um setor econômico.

| Sinal | Interpretação possível | Limitação |
|:--|:--|:--|
| Coincidência de datas | Compatível com oportunidade política | Correlação temporal não estabelece autoria |
| Ferramentas previamente usadas por um grupo | Pode sugerir sobreposição de procedimentos | Reutilização, vazamentos e imitação são possíveis |
| Declaração de fonte governamental | Evidência importante sobre avaliação oficial | Fonte, escopo e grau de divulgação precisam constar |
| Ausência de observação técnica independente | Reduz a robustez da atribuição | Não equivale a prova de ausência |

**Produto:** três hipóteses concorrentes, tabela de evidências contra cada uma e nota explícita de confiança.

## Caso C · Shadow Brokers e consequências históricas

O episódio envolvendo divulgações atribuídas ao grupo conhecido como Shadow Brokers é um tema legítimo de **história das ameaças, governança de vulnerabilidades e impacto sistêmico**. A utilidade aqui é compreender o que mudou para priorização de patches, compartilhamento de alertas e preparação de resposta.

**Recorte seguro para pesquisa:**
- Construir uma linha do tempo a partir de boletins oficiais e reportagens de fontes identificadas.
- Distinguir a divulgação de ferramentas, a existência de uma vulnerabilidade, sua exploração e as ações de mitigação.
- Discutir o impacto da exposição de ferramentas sofisticadas sobre programas de defesa.
- Evitar vincular cópias de ferramentas vazadas, coleções de exploits, varredores intrusivos ou orientações de execução.

**Ponto de partida:** [CISA](https://www.cisa.gov/), [Microsoft Security Response Center](https://msrc.microsoft.com/) e [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog). Procure os boletins históricos pertinentes e confira sempre as datas primárias, em vez de adotar cronologias de terceiros sem revisão.

## Quadro comum de avaliação

| Item | Exigência |
|:--|:--|
| Pergunta | Uma decisão explícita que o caso informa |
| Evidências | Fonte identificada, data de evento e data de publicação |
| Alternativas | Pelo menos duas interpretações plausíveis |
| Falsificabilidade | O que enfraqueceria a interpretação preferida? |
| Confiança | Uma justificativa textual, não apenas um rótulo |
| Recomendação | Medidas legais, proporcionais e defensivas |

Para publicar o resultado, use o [modelo de relatório](06-relatorios.md).

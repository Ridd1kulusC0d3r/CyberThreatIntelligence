# 08 · Auditoria das fontes, créditos e critérios de exclusão

[← Geopolítica](07-geopolitica-e-atribuicao.md) · [Início](../README.md)

**Revisão editorial:** 18/10/2026. A avaliação representa adequação ao objetivo **Threat Intelligence Links & Study**, não auditoria completa do código, da segurança ou da exatidão de cada conteúdo externo.

## Repositórios enviados para avaliação

| Fonte | Resultado | Motivo e destino |
|:--|:--|:--|
| [Daniel Donda / Cyber-Threat-Intelligence](https://github.com/danieldonda/Cyber-Threat-Intelligence) | **Integrado como referência** | Boa porta de entrada para fundamentos, hipóteses de hunting, modelos, geopolítica; nosso texto é original e revisa simplificações |
| [Sh4dow-BR / linkscyberthreatintelligence](https://github.com/Sh4dow-BR/linkscyberthreatintelligence) | **Integrado seletivamente** | O melhor é a curadoria de trilhas, livros, podcasts, cursos e recursos de prática; links duplicados e encurtadores foram excluídos |
| [Sh4dow-BR / sigma](https://github.com/Sh4dow-BR/sigma) | **Referência ao upstream** | É um fork; favorecer [SigmaHQ/sigma](https://github.com/SigmaHQ/sigma) como fonte oficial |
| [Sh4dow-BR / sigma-cli](https://github.com/Sh4dow-BR/sigma-cli) | **Referência ao upstream** | Fork; não acrescenta diferencial editorial suficiente ao catálogo básico |
| [Sh4dow-BR / LOOBins](https://github.com/Sh4dow-BR/LOOBins) | **Referência ao upstream** | Fork da iniciativa LOOBins, útil para o contexto de macOS |
| [Sh4dow-BR / ShadowS3Buckets](https://github.com/Sh4dow-BR/ShadowS3Buckets) | **Fora do núcleo CTI** | Verificação de configuração AWS pertence mais à gestão de postura de nuvem |
| [Sh4dow-BR / Zab-Prox-Agent](https://github.com/Sh4dow-BR/Zab-Prox-Agent) | **Fora do núcleo CTI** | Automação de Zabbix, sem ligação direta com o método de inteligência |
| [gameworkerkim / CTI Reports](https://github.com/gameworkerkim/CYBER-THREAT-INTELLIGENCE-REPORT) | **Modelo editorial, não evidência automática** | Inspira campos de relatório, resumo e categorização. Cada alegação do acervo exige confirmação primária independente |
| fastfire / deepdarkCTI | **Somente conceito de curadoria** | A categoria de análise de fontes de ambientes de risco é relevante, mas não copiamos diretórios de canais ilícitos, mercados, vazamentos ou métodos de acesso |
| [Vaskar71 / Detection Dashboard](https://github.com/Vaskar71/Cybersecurity-Threat-Detection-and-Response-Dashboard) | **Excluído do catálogo principal** | Exemplo didático de alertas com dados simulados, não valida coleta de inteligência do mundo real |
| GitHub topic “shadowbrokers” | **Somente estudo histórico** | Parte dos itens é material de exploração ou espelhos de vazamentos: não é apropriado para este acervo educacional defensivo; ver [estudo histórico](05-estudos-de-caso.md) |

## O que foi aproveitado e o que mudou

### Daniel Donda

**Aproveitado:** mapa de assuntos e fontes de base (threat hunting, APT, TTPs, MITRE, D3FEND, contexto geopolítico).  
**Recriado:** explicações próprias, distinções entre IOC, técnica e avaliação, tabela de evidências, hipóteses concorrentes e fluxo com PIR.  
**Corrigido na abordagem:** evitar apresentar indicadores como necessariamente reativos, heurísticas como certezas e atribuição estatal como equivalência automática a APT.

### Sh4dow-BR

**Aproveitado:** taxonomia editorial de livros, estudos, cursos, fontes, podcasts e materiais de prática.  
**Recriado:** anotações do porquê estudar, sequência de maturidade, deduplicação e advertências de uso.  
**Deixado de fora:** links de afiliados encurtados, duplicações, serviços sem documentação suficiente e conteúdo lateral sem aplicação real à CTI.

### Outros projetos

**gameworkerkim:** a ideia de metadados de relatórios é útil; não copiamos o template nem afirmamos validade de relatos apenas porque foram publicados.  
**deepdarkCTI:** metodologias de qualificação de fontes são relevantes; o catálogo não distribui caminhos a mercados ou conteúdo ilícito.  
**Dashboard simulado:** bom para estudo de interface, mas inadequado como fonte de indicadores ou evidência de detecção real.

## Proveniência e direitos autorais

- O texto autoral deste projeto foi escrito de forma independente, sem reproduzir a redação original dos repositórios referenciados.
- Links e títulos identificam obras externas; direitos permanecem com os respectivos titulares.
- A ausência de licença explícita em um repositório não concede permissão para copiar conteúdo.
- Imagens, dashboards, livros, PDFs e relatórios externos **não** devem ser espelhados sem verificação de licença.
- Este repositório ainda não declara uma licença para o seu próprio conteúdo. A escolha deve ser explícita pelo mantenedor.

## Critérios para futuras inclusões

**Incluir:** originalidade, fonte oficial, documentação utilizável, caso de uso CTI, atualização identificável, produção educacional verificável e segurança.  
**Investigar antes:** duplicações, repos sem licença, coleta de terceiros, feeds sem metodologia, excesso de marketing e análises baseadas em uma única fonte.  
**Excluir:** coleções de credenciais, dados privados, exploração ativa, malware executável, conteúdo ilegal e links cuja única função seja conduzir o leitor a tais materiais.

O objetivo é **profundidade e confiabilidade**, não maximizar o contador de URLs.

# 03 · Fontes e ferramentas comentadas

> Critério de entrada: autoridade, aplicação direta à CTI, documentação acessível e benefício adicional ao acervo. Links são atalhos para estudo, não endosso de todo conteúdo publicado por terceiros.

[← Método](02-metodologia.md) · [Trilhas →](04-trilhas.md) · [Catálogo legível por máquinas](../resources/catalog.json)

## 1. Fundamentos, modelos e padrões

| Fonte | Para estudar | Observação crítica |
|:--|:--|:--|
| [MITRE ATT&CK](https://attack.mitre.org/) | TTPs, técnicas, campanhas e grupos | Mapeamentos precisam de evidência comportamental |
| [MITRE CTI Training](https://attack.mitre.org/resources/training/cti/) | Análise de narrativas e recomendações | Exercícios oficiais usam versão anterior do ATT&CK |
| [ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/) | Matrizes, camadas e comparação visual | Visualização não comprova cobertura |
| [MITRE D3FEND](https://d3fend.mitre.org/) | Contramedidas e relacionamentos defensivos | Não substitui avaliação de eficácia |
| [OASIS CTI / STIX / TAXII](https://oasis-open.github.io/cti-documentation/) | Linguagem e transporte de CTI | Protocolos não garantem qualidade do dado |
| [FIRST TLP 2.0](https://www.first.org/tlp/) | Regras de divulgação e redistribuição | TLP:CLEAR substituiu o antigo TLP:WHITE |
| [Pyramid of Pain](https://www.sans.org/tools/the-pyramid-of-pain/) | Valor e resiliência de indicadores | Conceito orientador, não métrica exata |

## 2. Bases públicas, observáveis e pesquisa

| Fonte | Finalidade | Cuidado |
|:--|:--|:--|
| [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) | Exploração conhecida e priorização | Combinar com exposição local |
| [NVD](https://nvd.nist.gov/) | Registros e enriquecimento de CVEs | CVSS sozinho não mede risco empresarial |
| [VirusTotal](https://www.virustotal.com/gui/home/search) | Consulta de artefatos | Não submeter amostras ou dados confidenciais sem autorização |
| [AlienVault OTX](https://otx.alienvault.com/) | Pulses e indicadores comunitários | Conferir origem e recência |
| [URLhaus](https://urlhaus.abuse.ch/) | Pesquisa de URLs associadas a malware | Tratar indicadores como potencialmente perigosos; evitar visitas diretas |
| [Pulsedive](https://pulsedive.com/) | Contexto de observáveis | Analisar confiabilidade de associações |
| [Censys](https://search.censys.io/) | Panorama de serviços expostos | Investigação somente em escopo permitido |
| [Shodan](https://www.shodan.io/) | Contexto de exposição | Não equivale a permissão para interagir com sistemas |
| [APTnotes](https://github.com/kbandla/APTnotes) | Relatórios públicos e histórico | Usar como índice, citando documentos originais |

## 3. Plataformas e estruturação de CTI

| Projeto | Onde faz sentido |
|:--|:--|
| [MISP](https://github.com/MISP/MISP) | Modelos de evento, atributos, correlação e compartilhamento |
| [PyMISP](https://github.com/MISP/PyMISP) | Entender integração com a API do MISP |
| [OpenCTI](https://github.com/OpenCTI-Platform/opencti) | Construção de grafo de conhecimento e proveniência |
| [ATT&CK STIX Data](https://github.com/mitre-attack/attack-stix-data) | Dados oficiais estruturados em STIX 2.1 |
| [MITRE CTI (STIX 2.0)](https://github.com/mitre/cti) | Comparar o modelo legado com o mais recente |
| [MISP Galaxy](https://github.com/MISP/misp-galaxy) | Taxonomias, clusters e relações de entidades |

## 4. Investigação, detecção e documentação

| Projeto | Benefício | Limite |
|:--|:--|:--|
| [SigmaHQ](https://github.com/SigmaHQ/sigma) | Regras de detecção portáveis | Validar no ambiente e nos dados reais |
| [Sigma Specification](https://github.com/SigmaHQ/sigma-specification) | Conhecer semântica e formato | Não confundir regra com inteligência |
| [Threat Hunter Playbook](https://github.com/OTRF/ThreatHunter-Playbook) | Formular hipóteses e registrar raciocínio | Foco em hunting, complementar à CTI |
| [LOLBAS](https://lolbas-project.github.io/) | Contextualizar uso abusivo de ferramentas nativas | Consultar somente para defesa e análise |
| [LOOBins](https://loobins.io/) | Compreender artefatos nativos do macOS | Complementar, não eixo central |
| [The DFIR Report](https://thedfirreport.com/) | Narrativas de intrusão baseadas em investigações | Separar observação de generalização |

## 5. Trilhas editoriais e leitura guiada

- [Katie Nickels — CTI Self-Study, parte 1](https://medium.com/katies-five-cents/a-cyber-threat-intelligence-self-study-plan-part-1-968b5a8daf9a): mapa de estudo introdutório.
- [Katie Nickels — CTI Self-Study, parte 2](https://medium.com/katies-five-cents/a-cyber-threat-intelligence-self-study-plan-part-2-d04b7a529d36): evolução do repertório.
- [Andy Piazza — CTI Study Plan](https://klrgrz.medium.com/cyber-threat-intelligence-study-plan-c60484d319cb): organização de aprendizagem.
- [MITRE CTI Training](https://attack.mitre.org/resources/training/cti/): exercícios com objetivos explícitos.
- [SANS — Pyramid of Pain](https://www.sans.org/tools/the-pyramid-of-pain/): raciocínio sobre sinais defensivos.
- [No More Ransom](https://www.nomoreransom.org/): recursos públicos de conscientização e apoio defensivo.

### Livros para pesquisar em catálogos e bibliotecas

1. **Intelligence-Driven Incident Response**, Scott J. Roberts e Rebekah Brown. Integração entre inteligência e resposta.
2. **The Threat Intelligence Handbook**, Recorded Future. Introdução à prática e à operacionalização de CTI.
3. **Countdown to Zero Day**, Kim Zetter. Jornalismo de investigação sobre a dimensão histórica de operações cibernéticas.

A inclusão é bibliográfica; não estamos redistribuindo livros ou usando links encurtados de afiliados. Confirme edição e direitos de acesso com o editor ou biblioteca.

## 6. Relatórios e newsletters: como consumir

Priorize comunicados de [CISA](https://www.cisa.gov/), [CERT.br](https://www.cert.br/), [Mandiant](https://cloud.google.com/blog/topics/threat-intelligence), [Unit 42](https://unit42.paloaltonetworks.com/) e [Microsoft Threat Intelligence](https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/). São úteis para descoberta, mas continuam exigindo revisão crítica: um relatório de fornecedor pode empregar nomenclatura própria, ter cobertura incompleta ou não publicar as evidências brutas.

### Política de inclusão

O arquivo [resources/catalog.json](../resources/catalog.json) é a lista estruturada. Um link estar no catálogo **não significa** que seja um feed verificado continuamente. Para novas sugestões: registrar autor/proprietário, valor de estudo, tipo, nível de maturidade, linguagem, risco de manutenção e possível duplicação.

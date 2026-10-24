# Referências técnicas / Normas e RFCs

[← Início](../README.md) · [Trilha SOC](../learning-paths/soc-especialista.md)

Revisão editorial: **23/10/2026**. Referências oficiais e orientação pedagógica; não reproduzimos o texto integral das normas ISO. Conferir emendas e atualizações no catálogo oficial antes de uma implementação normativa.

## Normas e frameworks

| Referência | Papel | Aplicação no estudo |
|---|---|---|
| [ISO/IEC 27001:2022](https://www.iso.org/standard/27001) | Requisitos de SGSI; página oficial indica emenda | Relacionar escopo, riscos, objetivos e evidências |
| [ISO/IEC 27002:2022](https://www.iso.org/standard/75652.html) | Orientação sobre controles | Associar controles a práticas e evidências do SOC |
| [ISO 31000:2018](https://www.iso.org/standard/31000) | Diretrizes gerais de risco | Contexto, avaliação, tratamento, comunicação e revisão |
| [ISO/IEC 27005:2022](https://www.iso.org/standard/80585.html) | Gestão de risco de segurança da informação | Registro de risco e decisão de tratamento |
| [NIST SP 800-40 Rev. 4](https://csrc.nist.gov/pubs/sp/800/40/r4/final) | Planejamento de gestão empresarial de patches | Teste, implantação, exceção, rollback e verificação |
| [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) | Resposta integrada à gestão de risco; perfil CSF 2.0 | Preparação, detecção, resposta, recuperação e melhoria |
| [MITRE ATT&CK](https://attack.mitre.org/) | Comportamentos adversários observados | Mapear evidências, não palavras soltas |
| [MITRE D3FEND](https://d3fend.mitre.org/) | Conhecimento de técnicas defensivas | Justificar defesa e sua validação |

ISO 27001 estabelece requisitos; ISO 27002 orienta controles. ISO 31000 não é uma norma certificável de sistema de gestão. Um laboratório não demonstra conformidade organizacional. A 800-40 tem foco em patches e não cobre sozinha todo o programa de vulnerabilidades.

## Todas as RFCs citadas no perfil SOC

Prioridades abaixo são escolhas pedagógicas, não classificações oficiais do IETF. As páginas RFC Editor são a referência para status, errata e atualizações.

| RFC | Tema | Prioridade/contexto | Exercício |
|---|---|---|---|
| [1918](https://www.rfc-editor.org/info/rfc1918) | Endereçamento IPv4 privado | Essencial | Classificar endereços e evitar inferir origem pública a partir de IP privado. |
| [793](https://www.rfc-editor.org/info/rfc793) | TCP original | Histórica; substituída pela RFC 9293 | Comparar conceitos históricos com a especificação consolidada. |
| [768](https://www.rfc-editor.org/info/rfc768) | UDP | Essencial | Interpretar datagramas, portas e limites de observação. |
| [9293](https://www.rfc-editor.org/info/rfc9293) | TCP consolidado | Essencial | Explicar handshake, estados, retransmissão e encerramento. |
| [5716](https://www.rfc-editor.org/info/rfc5716) | Requisitos para sistemas de arquivos federados | Contextual | Relacionar disponibilidade e acesso a arquivos; não é uma RFC geral de TCP/IP. |
| [1034](https://www.rfc-editor.org/info/rfc1034) | Conceitos e facilidades do DNS | Essencial, com atualizações posteriores | Explicar resolução, delegação e cache. |
| [959](https://www.rfc-editor.org/info/rfc959) | FTP | Contextual/legado | Distinguir canal de controle e de dados; reconhecer exposição de protocolo legado. |
| [1035](https://www.rfc-editor.org/info/rfc1035) | Implementação e especificação DNS | Essencial, com atualizações posteriores | Interpretar consultas, respostas e tipos de registro. |
| [826](https://www.rfc-editor.org/info/rfc826) | ARP | Essencial em redes IPv4 locais | Relacionar IP/MAC e limites da evidência ARP. |
| [1102](https://www.rfc-editor.org/info/rfc1102) | Policy routing in Internet protocols | Discussão histórica, não padrão normativo | Discutir políticas de roteamento sem tratá-la como requisito operacional atual. |
| [2453](https://www.rfc-editor.org/info/rfc2453) | RIP versão 2 | Dependente do ambiente | Interpretar anúncios e limites de roteamento por distância. |
| [2674](https://www.rfc-editor.org/info/rfc2674) | Objetos gerenciados de bridges/VLANs | Histórica; substituída pela RFC 4363 | Entender MIBs e gerência; não confundir com a especificação IEEE de VLAN. |
| [2328](https://www.rfc-editor.org/info/rfc2328) | OSPF versão 2 | Dependente do ambiente | Explicar vizinhança, estado de enlace e impacto de falhas. |

**Correções importantes:** [RFC 9293](https://www.rfc-editor.org/info/rfc9293) substitui a RFC 793; [RFC 4363](https://www.rfc-editor.org/info/rfc4363) substitui a RFC 2674. A RFC 5716 trata de requisitos de sistemas de arquivos federados. A RFC 1102 declara que suas propostas não se destinam a ser padrões da Internet. Preservamos os números pedidos e contextualizamos sua utilidade.

## Método de leitura

Para cada protocolo: ler resumo, formato de mensagem, estados/fluxo relevante e considerações de segurança; relacionar a um pacote ou log; registrar o que a captura não mostra. Não é necessário decorar o documento inteiro. RFCs antigas podem continuar relevantes, mas uma lista de vaga não substitui análise de status e contexto.

# 06 · Relatórios de Cyber Threat Intelligence

[← Casos](05-estudos-de-caso.md) · [Geopolítica →](07-geopolitica-e-atribuicao.md)

## Modelo editorial mínimo

1. **Título e data de corte:** assunto, autor, período examinado e data de atualização.
2. **TLP e público:** por exemplo, TLP:CLEAR para informação de distribuição pública, quando aplicável.
3. **PIR e sumário executivo:** pergunta e resposta principal em linguagem decisória.
4. **Contexto:** setor, ativos relevantes, fonte original e escopo.
5. **Evidências:** alegações individualizadas, URLs, datas e independência.
6. **Hipóteses concorrentes:** interpretação preferida, alternativas e evidência contrária.
7. **Avaliação:** confiança justificada, riscos e consequências.
8. **Ações recomendadas:** responsáveis genéricos, critérios de sucesso e urgência.
9. **Limitações:** dados não disponíveis, viés de seleção, lacunas de telemetria.
10. **Referências e versão:** origem rastreável, data de acesso, correções.

## Exemplo: avaliação de risco (fictícia)

**Título:** Reutilização de identidade visual em mensagens fraudulentas contra o setor fictício Boreal  
**Data de corte:** 18/10/2026 · **Marcação:** TLP:CLEAR · **Natureza:** caso didático sintético

**PIR:** existem informações suficientes para recomendar reforço de comunicação oficial?

**Sumário executivo:** as mensagens simuladas apresentam semelhanças de redação e identidade visual. Isso é suficiente para recomendar comunicação preventiva, mas insuficiente para atribuir a atividade a um ator comum.

**Confiança:** moderada sobre a semelhança observada dentro do conjunto artificial; baixa sobre coordenação e autoria. As mensagens são exemplos produzidos para estudo, não evidências de incidentes.

**Ação:** utilizar canais oficiais de validação de comunicados, promover conscientização e registrar relatórios públicos antes de qualquer atribuição.

**Limitação:** não há coleta de campo, telemetria real nem fontes independentes neste cenário.

## TLP 2.0 e qualidade do compartilhamento

Consulte a definição [FIRST TLP](https://www.first.org/tlp/) antes de divulgar materiais. Os rótulos atuais incluem TLP:RED, TLP:AMBER, TLP:GREEN e TLP:CLEAR; há também a restrição TLP:AMBER+STRICT. **TLP não autoriza republicação de material protegido por direito autoral nem torna dados pessoais publicáveis.**

## Checklist para revisão por pares

- [ ] PIR explícito e recomendação correspondente.
- [ ] Alegações importantes com pelo menos uma referência verificável.
- [ ] Datas de publicação e observação diferenciadas.
- [ ] Incerteza, lacunas e explicações alternativas documentadas.
- [ ] Nomenclaturas de grupos usadas com cuidado, com equivalências atribuídas a fontes.
- [ ] Links seguros, sem indicadores clicáveis perigosos ou material restrito.
- [ ] Registro de revisão e possíveis correções.

## Frontmatter opcional para relatórios

```yaml
---
title: "Título do relatório"
description: "Resumo claro do tema e da conclusão"
date: "AAAA-MM-DD"
updated: "AAAA-MM-DD"
author: "Autor do relatório"
language: "pt-BR"
tlp: "CLEAR"
confidence: "moderada"
status: "analise"
tags: ["cti", "analise"]
---
```

O esquema é uma sugestão editorial, **não** afirma conformidade integral com STIX, TAXII, OpenCTI ou TLP.


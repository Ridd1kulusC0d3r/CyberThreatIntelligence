# Contribuições para CyberThreatIntelligence

Obrigado por ajudar a construir um acervo útil. Este é um projeto editorial de **formação, pesquisa defensiva, curadoria de CTI e laboratórios reproduzíveis**, não uma coleção irrestrita de links.

## Como sugerir um recurso

Abra uma issue ou pull request apresentando:

- **Título, URL canônica e autor/instituição.**
- **Categoria e nível** (iniciante, intermediário, avançado ou todos).
- **Utilidade concreta:** qual competência CTI desenvolve?
- **Proveniência:** publicação original ou índice de terceiros?
- **Data e status:** fonte ativa, histórica, mantida ou desconhecida?
- **Restrições:** licença, TLP, paywall ou condições de uso, quando pertinentes.

Antes de enviar, verifique se a URL já está no [catálogo JSON](resources/catalog.json) e explique por que merece inclusão.

## Política editorial

Priorize padrões oficiais, fontes independentes documentadas e estudos com metodologia explícita. Não copie conteúdo externo em bloco e não confunda nomes de grupos de fornecedores com identidade comprovada. Ações ofensivas, credenciais, dados vazados, amostras executáveis e diretórios de serviços ilícitos estão fora de escopo.

Nunca exponha tokens, informações pessoais ou dados confidenciais em issues e PRs. Exemplos devem ser sintéticos ou devidamente autorizados, sempre com dados minimizados.

## Testar o acervo

```bash
python3 scripts/validate_catalog.py
```

Esse teste verifica **estrutura e consistência**, não a disponibilidade dos sites nem a veracidade de alegações. Revisão editorial humana continua obrigatória.

## Padrão de escrita

Explicite a pergunta de inteligência, diferencie observação de inferência, acrescente hipóteses alternativas, justifique a confiança e cite fontes originais. Em conteúdos derivados de referências, escreva com suas próprias palavras e atribua a inspiração. Não publique alegações geopolíticas categóricas sem evidências substanciais.


## Contribuir com módulos e laboratórios

Defina objetivo, pré-requisito, tempo estimado, leitura primária, procedimento, entrega e critérios. Distinga exercício guiado de integração executável. Inclua dados sintéticos com proveniência, casos negativos e limites do teste. Normas devem ter edição/revisão; preserve a referência solicitada e explique substituições. Nunca declare teste não executado ou conformidade organizacional derivada de um exercício.

Antes de publicar, execute também:

```bash
python3 scripts/validate_learning.py
python3 scripts/run_soc_lab.py
python3 scripts/collect_fixture.py --self-test
```

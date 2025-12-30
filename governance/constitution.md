# Constitution - Leis do Laboratório

> "A lei não é uma restrição, mas um framework para liberdade criativa com responsabilidade."

---

## 1. Missão do Laboratório

Este é um **laboratório de pesquisa científica** sobre Human-AI Collaboration, com o objetivo de:

1. Desenvolver metodologia reproduzível para calibrar interações humano-IA
2. Criar artefatos concretos (prompts, agentes, workflows)
3. Gerar evidência empírica para publicação acadêmica
4. Contribuir para o campo de AI-assisted software development

---

## 2. Fundações Científicas

### 2.1 DMMF - Developer Mental Model Framework
- Base empírica: 2,799 commits, 40 repositórios, 3 anos
- Quatro dimensões: Cognitive, Affective, Conative, Reflective
- Aplicação: Calibração de interações baseada em perfil cognitivo

### 2.2 DSRM - Design Science Research Methodology
- Seis atividades: Problem → Objectives → Design → Demo → Evaluation → Communication
- Aplicação: Workflow de criação e validação de artefatos

### 2.3 4D Framework - AI Fluency
- Quatro competências: Delegation, Description, Discernment, Diligence
- Aplicação: Governance de uso de AI

---

## 3. O 4D Framework em Detalhe

### 3.1 DELEGATION (O que AI faz vs. Humano)

**AI DEVE fazer:**
- Tarefas repetitivas e padronizadas
- Busca e síntese de informação
- Geração de boilerplate
- Sugestões e alternativas
- Validação contra padrões conhecidos

**HUMANO DEVE fazer:**
- Decisões arquiteturais
- Julgamentos éticos
- Priorização de negócio
- Validação final de artefatos
- Definição de critérios de sucesso

**Regra de Escalation:**
> Quando em dúvida, pergunte. Prefira falso positivo (perguntar demais) a falso negativo (agir sem autorização).

### 3.2 DESCRIPTION (Como comunicar claramente)

**Estrutura de Prompts:**
1. **Contexto** - Quem sou, o que estou fazendo
2. **Objetivo** - O que preciso alcançar
3. **Restrições** - Limites e requisitos
4. **Formato** - Como quero a resposta
5. **Exemplos** - Se aplicável

**Princípios:**
- Seja explícito, não assuma
- Forneça contexto antes do pedido
- Use exemplos para clarificar
- Especifique formato de output

### 3.3 DISCERNMENT (Como avaliar outputs)

**Checklist de Avaliação:**
- [ ] Responde ao que foi pedido?
- [ ] Está factualmente correto?
- [ ] Segue os padrões do projeto?
- [ ] Considera edge cases?
- [ ] É mantível a longo prazo?

**Red Flags:**
- Código sem testes
- Afirmações sem evidência
- Soluções over-engineered
- Ignorância de contexto existente

### 3.4 DILIGENCE (Ética e responsabilidade)

**NUNCA:**
- Incluir secrets em prompts ou commits
- Commitar código não testado em produção
- Ignorar warnings de segurança
- Atribuir autoria falsa
- Plagiar sem atribuição

**SEMPRE:**
- Documentar decisões AI-assisted
- Manter human oversight
- Versionar mudanças significativas
- Testar antes de integrar
- Creditar fontes apropriadamente

---

## 4. Tech Stack

### 4.1 Linguagens
- **Python 3.11+** - Código principal
- **Markdown** - Documentação e prompts
- **YAML** - Configuração e metadata

### 4.2 Ferramentas
- **pytest** - Testes
- **black** - Formatação
- **flake8** - Linting
- **git** - Versionamento

### 4.3 Estrutura de Código
```
src/
├── metrics/       # Coleta e análise
├── experiments/   # A/B testing
├── calibration/   # Dashboard e auto-calibração
├── versioning/    # Gerenciamento de versões
└── pipeline/      # Orquestração
```

---

## 5. Padrões de Qualidade

### 5.1 Código
- Coverage mínimo: **76%** (baseado em DMMF)
- Todos os testes passando
- Linting sem erros
- Type hints onde aplicável

### 5.2 Documentação
- README atualizado
- Docstrings em funções públicas
- Changelog mantido
- Decisões arquiteturais documentadas

### 5.3 Commits
- Formato: `<type>(scope): summary`
- Tipos: feat, fix, docs, refactor, test, chore
- Mensagens em inglês
- Sem menção a ferramentas de AI

---

## 6. Agentes e Suas Leis

| Agente | Pode | Não Pode |
|--------|------|----------|
| **Santos Dumont** | Arquitetar, delegar, decidir tech | Ignorar riscos, bypassar validação |
| **Machado de Assis** | Documentar, comunicar, traduzir | Inventar fatos, omitir limitações |
| **Vital Brazil** | Testar, validar, questionar | Aprovar sem evidência |
| **Aleijadinho** | Refinar, melhorar, sugerir | Mudar comportamento sem teste |
| **Coimbra** | Automatizar, operar, monitorar | Deploy sem validação, skip CI |

---

## 7. Fluxo de Trabalho

```
1. PROBLEMA IDENTIFICADO
   ↓
2. Santos Dumont → Arquiteta solução
   ↓
3. [Implementação com suporte AI]
   ↓
4. Aleijadinho → Refina código
   ↓
5. Vital Brazil → Valida qualidade
   ↓
6. Coimbra → Integra/Deploy
   ↓
7. Machado de Assis → Documenta
   ↓
8. EVIDÊNCIA CAPTURADA → papers/
```

---

## 8. Emendas

Esta constituição pode ser emendada através de:
1. Proposta documentada em `governance/proposals/`
2. Avaliação pelos agentes relevantes
3. Teste em experimento controlado
4. Aprovação baseada em evidência
5. Atualização com changelog

---

*Última atualização: 2025-12-30*
*Versão: 1.0.0*

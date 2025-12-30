# Fluxo Informacional: Scripts Python no Lab

## Componentes Python Existentes

```
FERRAMENTAS PYTHON ATUAIS
=========================

evidence/
├── metrics/
│   ├── __init__.py
│   └── interaction_analyzer.py   # Coleta e análise de métricas
├── dashboard.py                   # Visualização
└── auto_calibration.py           # Sugestões automáticas

experiments/
├── __init__.py
└── experiment_runner.py           # Execução de experimentos A/B

anderson_skill/
└── meta/
    └── version_manager.py         # Versionamento de prompts

tests/                             # 7 arquivos de teste
├── test_interaction_analyzer.py
├── test_experiment_runner.py
├── test_version_manager.py
├── test_dashboard.py
├── test_integration_pipeline.py
└── test_integration_real_data.py

integration_pipeline.py            # Pipeline principal
setup.py                           # Configuração
```

---

## Fluxo Informacional Completo

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         FLUXO DE DADOS NO LABORATÓRIO                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────┐                                                        │
│  │  1. INTERAÇÃO   │  Humano + AI trabalhando juntos                        │
│  │     HUMANO-AI   │  (usando prompts de artifacts/)                        │
│  └────────┬────────┘                                                        │
│           │                                                                 │
│           ▼                                                                 │
│  ┌─────────────────────────────────────────────────────────────┐           │
│  │  2. COLETA DE DADOS (interaction_analyzer.py)                │           │
│  │     ├── Métricas de qualidade da resposta                   │           │
│  │     ├── Tempo de iteração                                    │           │
│  │     ├── Padrões de sucesso/falha                            │           │
│  │     └── Contexto utilizado                                   │           │
│  └────────┬────────────────────────────────────────────────────┘           │
│           │                                                                 │
│           ▼                                                                 │
│  ┌─────────────────────────────────────────────────────────────┐           │
│  │  3. ARMAZENAMENTO (evidence/)                                │           │
│  │     ├── evidence/patterns/     → Padrões identificados      │           │
│  │     ├── evidence/interactions/ → Exemplos good/bad          │           │
│  │     └── evidence/data/         → Dados brutos               │           │
│  └────────┬────────────────────────────────────────────────────┘           │
│           │                                                                 │
│           ▼                                                                 │
│  ┌─────────────────────────────────────────────────────────────┐           │
│  │  4. EXPERIMENTAÇÃO (experiment_runner.py)                    │           │
│  │     ├── Define hipóteses em experiments/hypotheses/         │           │
│  │     ├── Executa variantes A/B                               │           │
│  │     ├── Coleta resultados                                    │           │
│  │     └── Gera análise estatística                            │           │
│  └────────┬────────────────────────────────────────────────────┘           │
│           │                                                                 │
│           ▼                                                                 │
│  ┌─────────────────────────────────────────────────────────────┐           │
│  │  5. ANÁLISE (dashboard.py + auto_calibration.py)             │           │
│  │     ├── Visualiza tendências                                 │           │
│  │     ├── Identifica áreas de melhoria                        │           │
│  │     └── Sugere calibrações automáticas                      │           │
│  └────────┬────────────────────────────────────────────────────┘           │
│           │                                                                 │
│           ▼                                                                 │
│  ┌─────────────────────────────────────────────────────────────┐           │
│  │  6. EVOLUÇÃO (version_manager.py)                            │           │
│  │     ├── Versiona mudanças em prompts                        │           │
│  │     ├── Atualiza artifacts/prompts/                         │           │
│  │     └── Registra changelog                                   │           │
│  └────────┬────────────────────────────────────────────────────┘           │
│           │                                                                 │
│           ▼                                                                 │
│  ┌─────────────────────────────────────────────────────────────┐           │
│  │  7. VALIDAÇÃO (tests/)                                       │           │
│  │     ├── pytest tests/                                        │           │
│  │     ├── Verifica integridade do sistema                     │           │
│  │     └── Coverage > 76%                                       │           │
│  └────────┬────────────────────────────────────────────────────┘           │
│           │                                                                 │
│           ▼                                                                 │
│  ┌─────────────────────────────────────────────────────────────┐           │
│  │  8. PUBLICAÇÃO (papers/)                                     │           │
│  │     ├── Dados → Figuras                                      │           │
│  │     ├── Resultados → Seções do paper                        │           │
│  │     └── Insights → Contribuições                            │           │
│  └─────────────────────────────────────────────────────────────┘           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Mapeamento: Script → Papel no Fluxo

| Script | Papel | Input | Output |
|--------|-------|-------|--------|
| `interaction_analyzer.py` | **Coletor** | Logs de interação | Métricas estruturadas |
| `experiment_runner.py` | **Experimentador** | Hipóteses + variantes | Resultados estatísticos |
| `dashboard.py` | **Visualizador** | Métricas | Gráficos, relatórios |
| `auto_calibration.py` | **Calibrador** | Padrões | Sugestões de melhoria |
| `version_manager.py` | **Versionador** | Mudanças em prompts | Changelog, semver |
| `integration_pipeline.py` | **Orquestrador** | Tudo acima | Execução end-to-end |
| `tests/*.py` | **Validador** | Sistema completo | Pass/Fail, coverage |

---

## Nova Estrutura com Scripts Integrados

```
prompt-engineering-lab/
│
├── src/                            # CÓDIGO PYTHON (novo!)
│   ├── __init__.py
│   ├── metrics/                    # ← evidence/metrics/
│   │   ├── __init__.py
│   │   └── interaction_analyzer.py
│   ├── experiments/                # ← experiments/
│   │   ├── __init__.py
│   │   └── experiment_runner.py
│   ├── calibration/                # ← evidence/
│   │   ├── __init__.py
│   │   ├── dashboard.py
│   │   └── auto_calibration.py
│   ├── versioning/                 # ← anderson_skill/meta/
│   │   ├── __init__.py
│   │   └── version_manager.py
│   └── pipeline/
│       ├── __init__.py
│       └── integration_pipeline.py
│
├── tests/                          # TESTES (mantém estrutura)
│   ├── __init__.py
│   ├── test_metrics.py             # ← test_interaction_analyzer.py
│   ├── test_experiments.py         # ← test_experiment_runner.py
│   ├── test_calibration.py         # ← test_dashboard.py
│   ├── test_versioning.py          # ← test_version_manager.py
│   └── test_pipeline.py            # ← test_integration_pipeline.py
│
├── artifacts/                      # ARTEFATOS PRODUZIDOS
│   ├── prompts/
│   ├── agents/                     # Agentes brasileiros!
│   └── workflows/
│
├── evidence/                       # DADOS (não código)
│   ├── data/                       # Dados brutos e processados
│   ├── patterns/                   # Padrões documentados
│   ├── interactions/               # Exemplos good/bad
│   └── external/                   # anthropic-cookbook etc
│
├── experiments/                    # EXPERIMENTOS (não código)
│   ├── hypotheses/                 # Definições de experimentos
│   └── results/                    # Resultados
│
├── papers/                         # PUBLICAÇÕES
│   └── human-ai-collaboration/
│
├── research/                       # METODOLOGIA
│   └── methodology/
│
├── governance/                     # REGRAS
│
└── docs/                           # DOCUMENTAÇÃO
```

---

## Comandos de Execução (após reorganização)

```bash
# Coletar métricas de uma interação
python -m src.metrics.interaction_analyzer --collect

# Rodar experimento A/B
python -m src.experiments.experiment_runner --hypothesis ctx-performance-001

# Gerar dashboard
python -m src.calibration.dashboard --output evidence/data/reports/

# Sugerir calibrações
python -m src.calibration.auto_calibration --analyze

# Versionar mudança em prompt
python -m src.versioning.version_manager --bump minor

# Pipeline completo
python -m src.pipeline.integration_pipeline --full

# Rodar todos os testes
pytest tests/ -v --cov=src
```

---

## Agentes Brasileiros (como cidadao.ai)

| Papel | Craftsman Original | Versão Brasileira | Justificativa |
|-------|-------------------|-------------------|---------------|
| Tech Lead | Da Vinci | **Santos Dumont** | Inventor, visionário, polímata |
| Documentarian | Gutenberg | **Machado de Assis** | Maior escritor brasileiro |
| DevOps | Tesla | **Alberto Luiz Coimbra (COPPE)** | Engenheiro, fundador da COPPE |
| QA Engineer | Stradivari | **Vital Brazil** | Precisão, metodologia rigorosa |
| Code Reviewer | Michelangelo | **Aleijadinho** | Escultor, refinamento artístico |

Ou podemos usar um tema diferente - cientistas, músicos, etc. O que você prefere?

---

## Fluxo Visual Simplificado

```
INTERAÇÃO → COLETA → ARMAZENAMENTO → ANÁLISE → EVOLUÇÃO → PUBLICAÇÃO
    │          │           │            │          │           │
    │    interaction_   evidence/    dashboard   version_   papers/
    │    analyzer.py                 auto_cal    manager
    │          │           │            │          │           │
    │          └───────────┴────────────┴──────────┘           │
    │                       │                                   │
    │              tests/ (validação contínua)                 │
    │                       │                                   │
    └───────────────────────┴───────────────────────────────────┘
                    CICLO CONTÍNUO DE MELHORIA
```

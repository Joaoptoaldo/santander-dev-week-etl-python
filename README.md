# 🚀 Desafio DIO - ETL Profissional + Dashboard Streamlit

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Production-green.svg)](https://github.com/Joaoptoaldo/santander-dev-week-etl-python)

## Sobre

**Pipeline ETL completo** para Santander Dev Week replicado como portfólio.

**Fluxo**: CSV → Validação → Mensagens Personalizadas → Multi-formato (CSV/JSON/SQLite)

## Funcionalidades

- Extração flexível (CSV)
- Transformação com Jinja2 + validação pandas
- Carregamento multi-formato
- Métricas automáticas
- Análise interativa Plotly
- Dashboard Streamlit
- Arquitetura modular src/

## Como Usar

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Executar ETL
python main.py

# 3. Análise resultados
jupyter notebook notebooks/analise_dados.ipynb
```

## Estrutura

```
├── src/           # Módulos ETL
├── data/          # Entrada/saída
├── notebooks/     # Análise 
├── main.py        # Orquestrador
└── dashboard.py   # Streamlit Dashboard
└── requirements.txt
```

## Saídas Geradas

```
data/output/
├── clientes_enriquecidos.csv
├── clientes_enriquecidos.json
└── etl.db
```

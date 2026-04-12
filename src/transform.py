import pandas as pd
from jinja2 import Template
from typing import Dict

TEMPLATE = Template("Ola, {{ nome }}! Oportunidade: {{ produto }}. Conta {{ conta }} | Cartao {{ cartao }}.")

def validate_data(df: pd.DataFrame) -> pd.DataFrame:
    "Valida dados."
    required = ['nome', 'conta', 'cartao', 'produto']
    missing = [col for col in required if col not in df.columns]
    if missing:
        raise ValueError(f"Colunas ausentes: {missing}")
    df = df.dropna(subset=required)
    print(f"Dados validados: {len(df)} registros")
    return df

def generate_messages(df: pd.DataFrame) -> pd.DataFrame:
    "Gera mensagens."
    df_valid = validate_data(df)
    df_valid['mensagem'] = df_valid.apply(lambda row: TEMPLATE.render(**row), axis=1)
    print("Mensagens geradas")
    return df_valid

def etl_metrics(df_input: pd.DataFrame, df_output: pd.DataFrame) -> Dict:
    "Métricas."
    return {
        'registros_entrada': len(df_input),
        'registros_saida': len(df_output),
        'taxa_retencao': f"{len(df_output)/len(df_input)*100:.1f}%",
        'novas_colunas': ['mensagem']
    }

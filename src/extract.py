import pandas as pd
from pathlib import Path
from typing import Dict, List

def extract_csv(input_path: str = "data/input/clientes.csv") -> pd.DataFrame:
    "Extrai dados de CSV."
    path = Path(input_path)
    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")
    
    df = pd.read_csv(path)
    print(f"Extraídos {len(df)} registros de {path}")
    return df

def extract_fake_data(n: int = 20) -> pd.DataFrame:
    "Gera dados fake como fallback."
    nomes = [f"Cliente {i}" for i in range(1, n+1)]
    contas = [f"00{i:02d}-99" for i in range(1, n+1)]
    cartoes = [f"**** **** **** {i:04d}" for i in range(1, n+1)]
    produtos = ["cartão premium" if i%3==0 else "empréstimo" if i%3==1 else "investimentos" for i in range(1, n+1)]
    data = {
        "nome": nomes,
        "conta": contas,
        "cartao": cartoes,
        "produto": produtos
    }
    return pd.DataFrame(data)

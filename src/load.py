import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

def load_csv(df: pd.DataFrame, output_path: str = "data/output/clientes_enriquecidos.csv"):
    "Salva CSV."
    Path(output_path).parent.mkdir(exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Salvo CSV: {output_path}")

def load_json(df: pd.DataFrame, output_path: str = "data/output/clientes_enriquecidos.json"):
    "Salva JSON."
    Path(output_path).parent.mkdir(exist_ok=True)
    df.to_json(output_path, orient="records", indent=2)
    print(f"Salvo JSON: {output_path}")

def load_sqlite(df: pd.DataFrame, db_path: str = "data/output/etl.db", table: str = "clientes"):
    "Salva SQLite."
    Path(db_path).parent.mkdir(exist_ok=True)
    engine = create_engine(f"sqlite:///{db_path}")
    df.to_sql(table, engine, if_exists="replace", index=False)
    print(f"Salvo SQLite: {db_path}")

def multi_load(df: pd.DataFrame):
    "Multi formato."
    load_csv(df)
    load_json(df)
    load_sqlite(df)
    print("Carregamento concluido!")

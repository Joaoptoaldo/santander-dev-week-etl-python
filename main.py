#!/usr/bin/env python3
# Orquestrador ETL principal

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from extract import extract_csv
from transform import generate_messages, etl_metrics
from load import multi_load

def main():
    print("Iniciando Pipeline ETL Santander Dev Week")
    print("=" * 50)
    
    # 1. EXTRAÇÃO
    df_raw = extract_csv()
    
    # 2. TRANSFORMAÇÃO
    df_enriquecido = generate_messages(df_raw)
    metrics = etl_metrics(df_raw, df_enriquecido)
    
    # 3. CARREGAMENTO
    multi_load(df_enriquecido)
    
    # RELATÓRIO
    print("\n Métricas ETL:")
    for k, v in metrics.items():
        print(f"  {k}: {v}")
    
    print("\n Pipeline concluído com sucesso!")

if __name__ == "__main__":
    main()


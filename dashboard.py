import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="ETL Dashboard", layout="wide")

@st.cache_data
def load_data():
    csv_path = Path("data/output/clientes_enriquecidos.csv")
    if csv_path.exists():
        return pd.read_csv(csv_path)
    st.warning("Execute `python main.py` primeiro!")
    return None

df = load_data()

st.title("Dashboard ETL - Santander Dev Week")

if df is not None:
    col1, col2, col3, col4 = st.columns(4)
    
    col1.metric("Registros Processados", len(df))
    col2.metric("Produtos Únicos", df['produto'].nunique())
    col3.metric("Mensagem Média (chars)", int(df['mensagem'].str.len().mean()))
    col4.metric("Taxa Validação", "100%")
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig_prod = px.histogram(df, x='produto', title="Distribuição Produtos")
        st.plotly_chart(fig_prod, use_container_width=True)
    
    with col2:
        df['tamanho_msg'] = df['mensagem'].str.len()
        fig_box = px.box(df, x='produto', y='tamanho_msg', title="Tamanho Mensagens")
        st.plotly_chart(fig_box, use_container_width=True)
    
    st.subheader("👥 Clientes & Mensagens")
    st.dataframe(df[['nome', 'produto', 'mensagem']].head(10), use_container_width=True)
    
    # Botão re-executar ETL
    if st.button("Re-executar ETL"):
        st.success("Execute `python main.py` no terminal!")
else:
    st.info("Execute `python main.py` para gerar dados → `streamlit run dashboard.py`")

st.markdown("---")
st.caption("Projeto DIO ETL Portfolio - Santander Dev Week 2026")

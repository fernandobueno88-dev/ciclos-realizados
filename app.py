import streamlit as st
from funcoes.carregar import carregar_macros, carregar_viagens

st.set_page_config(
    page_title="Biomata Analytics",
    page_icon="🚛",
    layout="wide"
)

st.title("🚛 Biomata Analytics")

try:
    macros = carregar_macros()
    viagens = carregar_viagens()

    col1, col2 = st.columns(2)

    col1.metric("Macros", len(macros))
    col2.metric("Viagens", len(viagens))

    st.divider()

    st.subheader("Controle de Produção")
    st.dataframe(viagens)

    st.subheader("Macros")
    st.dataframe(macros)

except Exception as erro:
    st.error(erro)

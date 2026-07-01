import streamlit as st
from funcoes.carregar import carregar_macros, carregar_viagens

st.set_page_config(
    page_title="Biomata Analytics",
    page_icon="🚛",
    layout="wide"
)

st.title("🚛 Biomata Analytics")
st.subheader("Controle Operacional de Ciclos")

try:
    macros = carregar_macros()
    viagens = carregar_viagens()

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Registros de Macros", len(macros))

    with col2:
        st.metric("Viagens", len(viagens))

    st.divider()

    st.write("### Controle de Produção")
    st.dataframe(viagens.head())

    st.write("### Macros")
    st.dataframe(macros.head())

except Exception as e:
    st.error(f"Erro ao carregar as planilhas: {e}")

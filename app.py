import streamlit as st
from funcoes.carregar import carregar_macros, carregar_viagens

st.set_page_config(
    page_title="Biomata Analytics",
    page_icon="🚛",
    layout="wide"
)

st.title("🚛 Biomata Analytics")
st.subheader("Leitura das planilhas")

try:
    macros = carregar_macros()
    viagens = carregar_viagens()

    col1, col2 = st.columns(2)
    col1.metric("Registros de Macros", len(macros))
    col2.metric("Registros de Viagens", len(viagens))

    st.divider()

    st.write("### Viagens")
    st.dataframe(viagens.head(20), use_container_width=True)

    st.write("### Macros")
    st.dataframe(macros.head(20), use_container_width=True)

except Exception as e:
    st.error("Erro ao carregar as planilhas.")
    st.exception(e)

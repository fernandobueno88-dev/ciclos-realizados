import streamlit as st
from funcoes.carregar import carregar_macros, carregar_viagens
from funcoes.ciclos import montar_ciclos

st.set_page_config(
    page_title="Biomata Analytics",
    page_icon="🚛",
    layout="wide"
)

st.title("🚛 Biomata Analytics")
st.subheader("Ciclos realizados")

try:
    macros = carregar_macros()
    viagens = carregar_viagens()

    ciclos = montar_ciclos(viagens, macros)

    col1, col2, col3 = st.columns(3)

    col1.metric("Viagens", len(viagens))
    col2.metric("Macros", len(macros))
    col3.metric("Ciclos Montados", len(ciclos))

    st.divider()

    st.write("### Ciclos Identificados")
    st.dataframe(ciclos, use_container_width=True)

except Exception as e:
    st.error("Erro no sistema.")
    st.exception(e)

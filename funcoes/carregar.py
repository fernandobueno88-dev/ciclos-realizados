import pandas as pd
import os

PASTA_DADOS = "dados"

def carregar_macros():
    arquivo = os.path.join(PASTA_DADOS, "Relatório de Macro.xlsx")
    return pd.read_excel(arquivo)

def carregar_viagens():
    arquivo = os.path.join(PASTA_DADOS, "Controle de Produção.xlsx")
    return pd.read_excel(arquivo, sheet_name="Viagens")

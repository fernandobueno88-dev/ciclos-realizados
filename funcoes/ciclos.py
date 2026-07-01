import pandas as pd

def montar_ciclos(viagens, macros):
    viagens = viagens.copy()
    macros = macros.copy()

    viagens["INICIO DE VIAGEM"] = pd.to_datetime(viagens["INICIO DE VIAGEM"], errors="coerce")
    viagens["SAÍDA DESCARGA"] = pd.to_datetime(viagens["SAÍDA DESCARGA"], errors="coerce")
    macros["Data"] = pd.to_datetime(macros["Data"], errors="coerce")

    viagens["PREFIXO"] = viagens["PREFIXO"].astype(str).str.strip()
    macros["Frota"] = macros["Frota"].astype(str).str.strip()

    lista_ciclos = []

    for i, viagem in viagens.iterrows():
        prefixo = viagem["PREFIXO"]
        inicio = viagem["INICIO DE VIAGEM"]
        fim = viagem["SAÍDA DESCARGA"]

        if pd.isna(inicio) or pd.isna(fim):
            continue

        macros_ciclo = macros[
            (macros["Frota"] == prefixo) &
            (macros["Data"] >= inicio) &
            (macros["Data"] <= fim)
        ].sort_values("Data")

        lista_ciclos.append({
            "ID Ciclo": i + 1,
            "Prefixo": prefixo,
            "Motorista": viagem.get("MOTORISTA", ""),
            "Início Viagem": inicio,
            "Fim Viagem": fim,
            "Tempo Ciclo": fim - inicio,
            "Qtd Macros": len(macros_ciclo),
            "Macros": " | ".join(macros_ciclo["Nome da operação"].astype(str).tolist())
        })

    return pd.DataFrame(lista_ciclos)

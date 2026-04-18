import requests
import pandas as pd
import streamlit as st


@st.cache_data(ttl=300)

def get_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"

    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50,
        "page": 1
    }

    try:
        resposta = requests.get(url, params=params, timeout=10)
        resposta.raise_for_status()

        dados = resposta.json()

        if not isinstance(dados, list):
            return pd.DataFrame()

        df = pd.DataFrame(dados)

        # garante que colunas existem
        colunas = ["name", "current_price", "price_change_percentage_24h"]

        for col in colunas:
            if col not in df.columns:
                return pd.DataFrame()

        return df[colunas]

    except Exception as e:
        print("Erro API:", e)
        return pd.DataFrame()


# teste rápido (rodar esse arquivo sozinho)
if __name__ == "__main__":
    df = get_crypto_data()
    print(df[["name", "current_price", "price_change_percentage_24h"]])
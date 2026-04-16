import requests
import pandas as pd

def get_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"

    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50,
        "page": 1
    }

    resposta = requests.get(url, params=params)
    dados = resposta.json()

    df = pd.DataFrame(dados)

    return df


# teste rápido (rodar esse arquivo sozinho)
if __name__ == "__main__":
    df = get_crypto_data()
    print(df[["name", "current_price", "price_change_percentage_24h"]])
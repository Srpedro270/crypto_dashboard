import streamlit as st
from data.get_data import get_crypto_data

if "logado" not in st.session_state:
    st.session_state.logado = False

if not st.session_state.logado:
    st.title("🔐 Login")

    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if usuario == "admin" and senha == "123":
            st.session_state.logado = True
            st.success("Login realizado!")
            st.rerun()
        else:
            st.error("Usuário ou senha inválidos")

    st.stop()

st.title("📊 Crypto Dashboard")

with st.sidebar:
    st.write("Menu")

    if st.button("🚪 Logout"):
        st.session_state.logado = False
        st.rerun()

quantidade = st.slider("Quantidade de moedas", 5, 50, 10)

df = get_crypto_data()
df = df.head(quantidade)

# selecionar colunas importantes
df = df[["name", "current_price", "price_change_percentage_24h"]]

# métricas
maior_preco = df["current_price"].max()
media_preco = df["current_price"].mean()
maior_alta = df["price_change_percentage_24h"].max()

# layout em colunas
col1, col2, col3 = st.columns(3)

col1.metric("💰 Maior Preço", f"${maior_preco:.2f}")
col2.metric("📊 Média de Preço", f"${media_preco:.2f}")
col3.metric("🚀 Maior Alta (24h)", f"{maior_alta:.2f}%")


st.subheader("📊 Preço das Moedas")

grafico = df[["name", "current_price"]].set_index("name")
st.bar_chart(grafico)

st.dataframe(df)
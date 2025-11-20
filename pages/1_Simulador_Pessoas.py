import streamlit as st
import pandas as pd
from calculos import projetar_crescimento

st.title("Simulador de crescimento populacional")

st.sidebar.header("Configurações")
unidade = st.sidebar.selectbox("Unidade de Tempo", ["Ano", "Mês", "Semana", "Dia"])


st.sidebar.header("Parâmetros")
pop_ini = st.sidebar.number_input("Populacão atual", value=100)
taxa = st.sidebar.slider(f"Taxa de crescimento (%) -- {unidade}", 0.0, 50.0, 10.0)
periodos = st.sidebar.slider(f"Período de teste -- {unidade}", 1, 100, 10)

taxa_decimal = taxa / 100

lista_final = projetar_crescimento(pop_ini, taxa_decimal, periodos)

indicetabela = range(1, periodos + 1)

df = pd.DataFrame(
    {"Populacão": lista_final},
    index=indicetabela
)

df.index.name = unidade
st.write("### Dados Detalhados")
st.dataframe(df)

st.write("### Projeção Futura")
st.line_chart(df)


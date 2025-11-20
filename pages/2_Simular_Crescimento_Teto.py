import streamlit as st
import pandas as pd
from calculos import teto_crescimento

st.title("Simulador de crescimento com um valor limite")

st.info("**Atenção :** Ao utilizar o sistema no celular, clique na seta (>>) no canto superior esquerdo para alterar os dados da simulação!")

st.sidebar.header("Configurações")
unidade = st.sidebar.selectbox("Unidade de Tempo", ["Ano", "Mês", "Semana", "Dia"])

st.sidebar.header("Parâmetros")
pop_ini = st.sidebar.number_input("Espaço de ocupação atual", value=100)
max_limite = st.sidebar.number_input("Capacidade máxima suportada ", value = 1000)
taxa = st.sidebar.slider(f"Taxa de crescimento (%) -- {unidade}", 0.0, 50.0, 10.0)
periodos = st.sidebar.slider(f"Período de teste -- {unidade}", 1, 30, 10)


taxa_decimal = taxa / 100

lista_final = teto_crescimento(pop_ini, taxa_decimal, periodos,max_limite)

indice_tabela = range(1, periodos + 1)

df = pd.DataFrame(
    {"Populacão": lista_final},
    index=indice_tabela
)

df.index.name = unidade
st.write("### Dados Detalhados")
st.dataframe(df)

st.write("### Projeção Futura")
st.line_chart(df)
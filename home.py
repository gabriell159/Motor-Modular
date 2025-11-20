import streamlit as st

st.set_page_config(page_title="Motor Modular", page_icon="🚀")

st.title("🚀 Bem-vindo ao Motor Modular")
st.write("""
O **Motor Modular** é um projeto de simulação de cenários. 
O objetivo é projetar acontecimentos reais baseados em parâmetros fornecidos pelo usuário, 
permitindo a análise de diferentes futuros possíveis.
""")

st.divider()

st.header("🧰 Ferramentas Disponíveis")
st.write("Use o menu lateral para navegar entre os modelos:")

col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Crescimento Exponencial")
    st.caption("Simulador de Crescimento Populacional")
    st.write("""
    Projeção baseada em taxas compostas. Assume recursos infinitos: 
    quanto maior a população, mais rápido ela cresce. 
    A população nova é descrita pela multiplicação 
    da população atual pela taxa de crescimento.
    """)
    st.latex(r"P_{novo} = P_{atual} \times (1 + taxa)")

with col2:
    st.subheader("2. Crescimento Logístico")
    st.caption("Modelo de Verhulst (1838)")

    st.write("""
    Baseado na **Equação Logística de Pierre Verhulst**. 
    Diferente do exponencial, este modelo introduz a **Capacidade de Carga ($K$)**, 
    que representa o limite máximo de recursos do ambiente.
    """)

    st.write("**A Lógica do Freio:**")
    # A fórmula matemática elegante
    st.latex(r"f_{freio} = 1 - \frac{P_{atual}}{K_{teto}}")

st.divider()
st.info("👈 Selecione uma ferramenta no menu lateral para começar.")
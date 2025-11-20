
import streamlit as st

pagina_inicial = st.Page(
    "home.py",
    title="Motor Modular",
    icon="📊",
    default=True
)

pagina_simulador1 = st.Page(
    "pages/1_Simulador_Pessoas.py",
    title="Simulador de Crescimento Populacional",
    icon="👥"
)

pagina_simulador2 = st.Page(
    "pages/2_Simular_Crescimento_Teto.py",
    title="Simulador de crescimento com um valor limite",
    icon="👥"
)

pg = st.navigation(
    {
        "Home": [pagina_inicial],
        "Ferramentas": [pagina_simulador1, pagina_simulador2],
    }
)

pg.run()
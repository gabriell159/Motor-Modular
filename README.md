# 🚀 Motor Modular: Simulador de Cenários e Crescimento

> **Demo:** [Acesse o Simulador Aqui](https://motor-modular-3ppwxp8f6a8q4jahyc8pxm.streamlit.app/)

## 📖 Sobre o Projeto
O **Motor Modular** é uma aplicação web interativa desenvolvida em **Python** para simulação de cenários de crescimento. O projeto abstrai o conceito de tempo (dias/meses/anos), permitindo simular o crescimento de comunidades/espaços através de modelos matemáticos.

O diferencial deste projeto é a implementação de modelos matemáticos clássicos em uma interface moderna e intuitiva, focada na tomada de decisão baseada em dados.

---

## 🧰 Funcionalidades e Modelos

Atualmente o sistema conta com dois motores de simulação distintos:

### 1. Crescimento Exponencial
Simula cenários de **recursos infinitos**. Ideal para testes de crescimento simples.
- **Base Matemática:** Juros Compostos / Função Exponencial.
- **Fórmula:** $P_{t+1} = P_t \times (1 + taxa)$
- **Aplicação:** Startups em *early stage*, contágio viral inicial.

### 2. Crescimento Logístico
Implementação da **Equação Logística de Pierre Verhulst**. Introduz o conceito de **Capacidade de Carga ($K$)** ou "Teto".
- **Base Matemática:** Equação Diferencial Logística.
- **Destaque:** Algoritmo de "Freio" que calcula a saturação do ambiente.
- **Fórmula do Freio:** $1 - \frac{P_{atual}}{K_{teto}}$
- **Aplicação:** Saturação de mercado, lotação de espaços físicos, biologia populacional.

---

## 🛠️ Tecnologias Utilizadas

O projeto foi construído utilizando uma arquitetura modular para garantir escalabilidade.

- **Linguagem:** Python 3.13
- **Framework Web:** Streamlit (com uso da nova API `st.navigation`)
- **Manipulação de Dados:** Pandas (DataFrames e Séries Temporais)
- **Visualização:** Streamlit Native Charts & Matplotlib
- **Deploy:** Streamlit Community Cloud

---

## 📂 Arquitetura do Projeto

A estrutura segue o princípio de separação de responsabilidades, isolando a lógica matemática da interface do usuário.

```text
. (Raiz do Repositório)
│
├── pages/             # 🖥️ TELAS (Frontend)
│   ├── 1_Simulador_Pessoas.py
│   └── 2_Crescimento_Limitado.py
│
├── calculos.py        # 🧠 O CÉREBRO (Backend lógico)
├── menu.py            # 🚦 O ROTEADOR (Menu principal)
├── home.py            # 🏠 PÁGINA INICIAL (Textos e teoria)
├── requirements.txt   # 📦 DEPENDÊNCIAS
└── .gitignore
```

---

## 👨‍💻 Autor

Desenvolvido por **Gabriel Ferreira**

Entre em contato:
* [LinkedIn](https://www.linkedin.com/in/gabriel-ferreira-49520521a/)
* [GitHub](https://github.com/gabriell159)
* 📧 **gfo2130626@gmail.com**

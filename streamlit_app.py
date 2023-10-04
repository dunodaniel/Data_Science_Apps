import streamlit as st
from apps.projeto1 import exibir_projeto_1
from apps.projeto2 import exibir_projeto_2

# Configuração do cabeçalho
st.title("Meus Projetos Streamlit")

# Cria links para os projetos
projeto1 = st.sidebar.button("Projeto 1")
projeto2 = st.sidebar.button("Projeto 2")

# Projeto 1
if projeto1:
    exibir_projeto_1()
elif projeto2:
    exibir_projeto_2()

import streamlit as st
from apps.projeto1 import exibir_projeto_1
from apps.projeto2 import exibir_projeto_2

# Configuração do cabeçalho
st.title("Meus Projetos Streamlit")
st.header("Bem-vindo à minha página de projetos!")

# Breve apresentação
st.write("Olá! Sou [DunoDaniel](https://github.com/) e estou empolgado em compartilhar meus projetos com você.")
st.write("Nesta página, você encontrará dois dos meus projetos mais recentes.")
st.write("Sinta-se à vontade para explorar e experimentar cada projeto clicando nos botões à esquerda.")


# Cria links para os projetos
projeto1 = st.sidebar.button("Projeto 1")
projeto2 = st.sidebar.button("Projeto 2")

# Projeto 1
if projeto1:
    exibir_projeto_1()
elif projeto2:
    exibir_projeto_2()

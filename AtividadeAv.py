import streamlit as st 



st.title("Programa Aumento Salarial")


# container = st.container (border=True) 
def ExibirDados():
  with st.container(border = True):
    Nome = st.text_input("Informe seu nome",)
  with st.container(border = True):
    DataNasc = st.date_input("Informe sua data de nascimento")
  with st.container(border = True):
    EstadoCivil = st.text_input("Informe seu estado cívil"(Solteiro, Casado, Divorciado, Viúvo))


ExibirDados()

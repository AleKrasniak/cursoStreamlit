import streamlit as st 

print("peido")

st.title("Programa Aumento Salarial")


# container = st.container (border=True) 
with st.container(border = True):
  Nome = st.text_input("Informe seu nome","Nome")


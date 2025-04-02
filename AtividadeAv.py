import streamlit as st 



st.title("Programa Aumento Salarial")

def Calculos():
  
  



# container = st.container (border=True) 
def Main():
  with st.container(border = True):
    Nome = st.text_input("Informe seu nome",)
    
  with st.container(border = True):
    DataNasc = st.date_input("Informe sua data de nascimento")
    
  with st.container(border = True):
    EstadoCivil = st.selectbox(
      "Informe seu estado cívil", 
      ("Solteiro", "Casado", "Divorciado", "Viúvo"),
    )
    
  with st.container(border = True):
    Sexo = st.selectbox(
      "Informe seu gênero", 
      ("Masculino", "Feminino",),
    )
    
  with st.container(border = True):
    Salario = st.number_input(
      "Informe seu salário", 
    )
#SELECT BOX
Main()
def Calculos():
  if (Salario < 2.500.0):
    print("Deve receber Aumento")


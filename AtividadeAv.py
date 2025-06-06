import streamlit as st

st.title("Programa Aumento Salarial")
  
  
  # container = st.container (border=True) 
def main():
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
    if st.button("Consultar Aumento Salarial"): 
      if Salario < 2500:
        st.write("Deve receber Aumento")
        st.balloons()
        aumento = 0.0
        while (aumento < 500):
           aumento = aumento + 100
           salario = Salario + aumento
        st.write("Seu aumento foi de R$: ",aumento,)
        st.write("Seu salário atual é de R$ ",salario,)
          
      else:
        st.write("O Aumento não é necessário")
  
  
  
main()

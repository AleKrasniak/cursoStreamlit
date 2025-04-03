import streamlit as st 


# aumento = 0.0
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

open_modal = st.button("Teste")
if open_modal:
    modal.open()

  # if st.button("teste"): 
   if Salario < 2500:
    st.balloons() 
    st.write("Deve receber Aumento") 
     modal = Modal(
    "Demo Modal", 
    key="demo-modal",
    
    # Optional
    padding=20,    # default value
    max_width=744  # default value
)
if modal.is_open():
    with modal.container():
        st.write("Text goes here")

        st.write("Some fancy text")
        value = st.checkbox("Check me")
        st.write(f"Checkbox checked: {value}")
    

    aumento = 0.0
    while aumento < 500:
     aumento = aumento + 100
     st.write("Seu aumento foi de R$: ",aumento,)

   else:
    st.write("peido")



main()




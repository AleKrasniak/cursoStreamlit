import streamlit as st
st.header("Cabeçalho")

options = st.multiselect(
    "What are your favorite colors",
    ["Green", "Yellow", "Red", "Blue"],
    ["Yellow", "Red"],
)

st.checkbox('Sorvete')
st.checkbox('Café')
st.checkbox('Refrigerante')
    
st.toggle("Toggle")
st.button("Botão Salvar")
st.text_area("Adicione texto")
st.text_input("")
st.selectbox(
  'Do que é feito o Teteu?',
  ('Acuçar 100%','50% Acuçar','50% Açucar e 50% Mel'))

import streamlit as st
st.header("Cabeçalho")
st.multiselect(
  'Números da Mega Sena'
  ['31','62','98','100','20','12'],
  ['81','52'])
)
st.toggle("Toggle")
st.button("Botão Salvar")
st.text_area("Adicione texto")
st.text_input("")
st.selectbox(
  'Do que é feito o Teteu?',
  ('Acuçar 100%','50% Acuçar','50% Açucar e 50% Mel'))

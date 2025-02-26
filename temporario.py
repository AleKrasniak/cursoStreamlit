import streamlit as st
st.header("Cabeçalho")

st.multiselect(
    'Números da Mega Sena',
    ['45','78','96','20','21'],
    ['61','87'])

st.checkbox('Sorvete')
st.checkbox('Café')
st.checkbox9('Refrigerante')
    
st.toggle("Toggle")
st.button("Botão Salvar")
st.text_area("Adicione texto")
st.text_input("")
st.selectbox(
  'Do que é feito o Teteu?',
  ('Acuçar 100%','50% Acuçar','50% Açucar e 50% Mel'))

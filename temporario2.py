import streamlit as st

st.header("Informe Seus Dados")

col1, col2 = st.columns(2)

with col1:
  uploaded_files = st.file_uploader(
    "Escolha uma foto", accept_multiple_files=True
  )
  if file is not None: 
    try:
      uploaded = Image.open(uploaded_files)
    except: 
      st.error("Imagem não enviada")

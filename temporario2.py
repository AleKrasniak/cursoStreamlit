import streamlit as st

st.header("Informe Seus Dados")

col1, col2 = st.columns(2)

with col1:
  with st.expander:
    uploaded_files = st.file_uploader(
      "Escolha uma foto", accept_multiple_files=True
    )
    if uploaded_files is not None: 
      try:
        uploaded_files = Image.open(uploaded_files)
      except: 
        st.error("Imagem não enviada")

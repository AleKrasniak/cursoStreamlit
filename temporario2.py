import streamlit as st

st.header("Informe Seus Dados")

col1, col2 = st.columns(2)

with col1:
  uploaded_files = st.file_uploader(
    "Escolha uma foto", accept_multiple_files=True
  )

  for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write (bytes_data)

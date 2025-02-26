import streamlit as st
import pandas as pd
st.header("Cabeçalho")

options = st.multiselect(
    "What are your favorite colors",
    ["Green", "Yellow", "Red", "Blue"],
    ["Yellow", "Red"],
)

st.checkbox('Sorvete')
st.checkbox('Café')
st.checkbox('Refrigerante')

st.color_picker("Pick a color", "#00f900")
st.feedback("stars")

df = pd.DataFrame(
    [   
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.ballons", "rating": 5, "is_widget": True},
        {"command": "st.time_input", "rating": 3, "is_widget": False},
    ]
)

edited_df = st.data_editor(df)

nevinha = st.toggle("Toggle")
if nevinha:
    st.snow()
else
    st.write("Peidou na farofa")
    

st.button("Botão Salvar")
st.text_area("Adicione texto")
st.text_input("")
st.selectbox(
  'Do que é feito o Teteu?',
  ('Acuçar 100%','50% Acuçar','50% Açucar e 50% Mel'))

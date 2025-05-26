from transformers import pipeline
import streamlit as st
st.title("aplikasi sederhana")
st.write("ini adalah aplikasi sederhana")
# Buat pipeline NLP untuk analisis sentimen
classifier = pipeline("sentiment-analysis")

text_input = st.text_input("Insert a sentence")
if st.button("submit"):
# Analisis kalimat
    result = classifier(text_input)
    st.json(result)

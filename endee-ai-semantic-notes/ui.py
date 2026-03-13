import streamlit as st
import requests

st.title("AI Semantic Notes Assistant")

st.header("Upload Notes")
file_path = st.text_input("Enter PDF Path")

if st.button("Upload"):
    res = requests.post("http://127.0.0.1:8000/upload", params={"path": file_path})
    st.write(res.json())

st.header("Ask Question")
question = st.text_input("Enter Question")

if st.button("Ask"):
    res = requests.get("http://127.0.0.1:8000/ask", params={"q": question})
    st.write(res.json())
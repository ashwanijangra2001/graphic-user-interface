import streamlit as st
import function

todos = function.python_project()

st.title("To do app")
st.subheader("This is my todo list.")
st.write("This app is to increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder='Add new todo....')
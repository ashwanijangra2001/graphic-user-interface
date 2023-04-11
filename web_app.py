import streamlit as st
import function

todos = function.python_project()

st.title("MY TODO APP")
st.subheader("This is my todo app")
st.write("This app is increase the productivity:")

for todo in todos:
    st.checkbox(todo)


st.text_input(label='', placeholder='add a new todo...')






import streamlit as st

st.title("🤖 My Chatbot")

user_input = st.text_input("Ask me anything:")

if user_input:
    # ... run OpenAI API call and show result
    st.write(response)

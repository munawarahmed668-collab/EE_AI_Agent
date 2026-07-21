import streamlit as st

from ai.agent import process_question

st.set_page_config(
    page_title="Electrical Engineering AI Assistant",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Electrical Engineering AI Assistant")

st.write("Ask any Electrical Engineering question.")

question = st.text_input("Your Question")

if st.button("Ask AI"):
    if question.strip():
        with st.spinner("Thinking..."):
            answer = process_question(question)
        st.success(answer)
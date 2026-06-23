import streamlit as st
from utils.grammar_utils import check_grammar

st.title("Grammar Checker")

text = st.text_area("Enter text")

if st.button("Check Grammar"):
    corrected = check_grammar(text)

    st.subheader("Original Text")
    st.write(text)

    st.subheader("Corrected Text")
    st.success(corrected)
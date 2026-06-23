import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="AI Translator Suite",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS
with open("assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )


# Hero
st.markdown("""
<div class="glass-card">

<h1 style='text-align:center;
color:#38bdf8;
font-size:3rem;
font-weight:bold;'>
🤖 Sreenadh AI Language Studio
</h1>

<p style='text-align:center;
font-size:20px;
color:white;'>
By Sreenadh Gajjala
</p>

<p style='text-align:center;
color:#d1d5db;'>
AI-Powered Translation & Writing Assistant
</p>

</div>
""", unsafe_allow_html=True)
# Metrics
col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric("Languages", "100+")

with col2:
    st.metric("AI Tools", "8")


with col3:
    st.metric("Version", "1.0")
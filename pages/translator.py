import streamlit as st

st.markdown("""
<style>
...
""", unsafe_allow_html=True)

from utils.speech_utils import text_to_speech
import os
import streamlit as st
import pandas as pd
from datetime import datetime
from langdetect import detect
from utils.translator_utils import *

st.title("🌍 AI Translator")

languages = get_languages()
language_names = list(languages.keys())

source = st.selectbox(
    "Source Language",
    language_names,
    index=language_names.index("english")
)

target = st.selectbox(
    "Target Language",
    language_names,
    index=language_names.index("telugu")
)

text = st.text_area(
    "Enter Text",
    height=200
)

col1, col2 = st.columns(2)

with col1:
    detect_btn = st.button("🔍 Detect Language")

with col2:
    translate_btn = st.button("🌐 Translate")

if detect_btn:

    if text.strip():

        try:
            detected = detect(text)

            st.success(
                f"Detected Language Code: {detected}"
            )

        except:
            st.error("Unable to detect language.")

if translate_btn:

    if text.strip():

        translated = translate_text(
            text,
            source,
            target
        )

        st.success("Translation Complete")

        st.text_area(
           "Translated Text",
            translated,
            height=200,
            key="translated_output"
       )

        st.code(translated)

        audio_file = text_to_speech(translated)

        with open(audio_file, "rb") as f:
            audio_bytes = f.read()

        st.audio(audio_bytes)

        st.download_button(
           label="⬇ Download Audio",
           data=audio_bytes,
           file_name="translation.mp3",
           mime="audio/mp3"
) 
        history = pd.read_csv(
            "data/translation_history.csv"
        )

        history.loc[len(history)] = [
            datetime.now(),
            source,
            target,
            text,
            translated
        ]

        history.to_csv(
            "data/translation_history.csv",
            index=False
        )
        
        st.divider()

st.subheader("📊 Text Analytics")

if text:

    words = len(text.split())
    chars = len(text)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Words", words)

    with col2:
        st.metric("Characters", chars)
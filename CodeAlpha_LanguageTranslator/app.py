import streamlit as st
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import os

# Page title
st.title("🌍 AI Language Translator")
st.write("Translate text from one language to another")

translator = Translator()

# Language list
languages = list(LANGUAGES.values())

# Input text
text = st.text_area("Enter text to translate:")

# Language selection
source_lang = st.selectbox("Select Source Language", languages)
target_lang = st.selectbox("Select Target Language", languages)

# Convert language names to codes
def get_language_code(language_name):
    for code, name in LANGUAGES.items():
        if name == language_name:
            return code

# Translate button
if st.button("Translate"):
    if text == "":
        st.warning("Please enter text")
    else:
        src_code = get_language_code(source_lang)
        tgt_code = get_language_code(target_lang)

        translated = translator.translate(text, src=src_code, dest=tgt_code)

        st.success("Translation:")
        st.write(translated.text)

        # Copy feature
        st.code(translated.text)

        # Text to Speech feature
        tts = gTTS(translated.text, lang=tgt_code)
        tts.save("voice.mp3")
        st.audio("voice.mp3")
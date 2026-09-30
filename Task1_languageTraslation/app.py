import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌐"
)

st.title("🌐 Language Translation Tool")
st.write("Translate text from one language to another easily.")

languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "Arabic": "ar",
    "Russian": "ru"
}

text = st.text_area(
    "Enter text:",
    placeholder="Type your text here..."
)

col1, col2 = st.columns(2)

with col1:
    source_language = st.selectbox(
        "Source Language",
        list(languages.keys())
    )

with col2:
    target_language = st.selectbox(
        "Target Language",
        list(languages.keys()),
        index=1
    )

if st.button("Translate", type="primary"):
    if text.strip():
        try:
            translator = GoogleTranslator(
                source=languages[source_language],
                target=languages[target_language]
            )

            translated_text = translator.translate(text)

            st.subheader("Translated Text")
            st.success(translated_text)

        except Exception as e:
            st.error(f"Translation failed: {e}")
    else:
        st.warning("Please enter some text first.")

import streamlit as st

st.set_page_config(page_title="FAQ Chatbot", page_icon="🤖")

st.title("🤖 FAQ Chatbot")
st.write("Ask a question and get the most relevant answer.")

faq = {
    "what is python": "Python is a high-level, easy-to-learn programming language.",
    "what is streamlit": "Streamlit is a Python framework used to create web applications easily.",
    "what is machine learning": "Machine Learning is a branch of AI that allows computers to learn from data.",
    "what is artificial intelligence": "Artificial Intelligence is the simulation of human intelligence in machines.",
    "what is nlp": "NLP stands for Natural Language Processing. It helps computers understand human language.",
    "what is data science": "Data Science is the process of extracting useful information from data.",
    "what is github": "GitHub is a platform used to store, manage and collaborate on code.",
    "what is python used for": "Python is used for web development, AI, machine learning, data science and automation."
}

question = st.text_input("Ask your question:")

if st.button("Get Answer"):
    if question.strip():
        question_lower = question.lower()

        best_answer = None

        for key, answer in faq.items():
            if key in question_lower or question_lower in key:
                best_answer = answer
                break

        if best_answer:
            st.success(best_answer)
        else:
            st.warning("Sorry, I could not find a relevant answer.")
    else:
        st.warning("Please enter a question.")

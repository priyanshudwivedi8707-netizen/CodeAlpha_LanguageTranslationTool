import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

st.set_page_config(page_title="FAQ Chatbot", page_icon="🤖")

st.title("🤖 FAQ Chatbot")
st.write("Ask a question and get the most relevant answer.")

faq_data = {
    "What is CodeAlpha?":
        "CodeAlpha is a software development company that provides internship and learning opportunities.",

    "How can I join the internship?":
        "You can join the internship by following the instructions provided by CodeAlpha.",

    "What projects are available?":
        "AI interns can work on projects such as Language Translation, FAQ Chatbot, Music Generation, and Object Detection.",

    "How do I submit my project?":
        "Upload your complete source code to GitHub and submit the GitHub repository link through the submission form.",

    "What is an AI chatbot?":
        "An AI chatbot is a software application that interacts with users and provides responses to their questions.",

    "What is NLP?":
        "NLP stands for Natural Language Processing. It helps computers understand and process human language.",

    "What is machine learning?":
        "Machine learning is a branch of AI that enables computers to learn patterns from data and make predictions."
}

def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text

questions = list(faq_data.keys())
processed_questions = [preprocess(q) for q in questions]

vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(processed_questions)

def get_answer(user_question):
    processed_input = preprocess(user_question)
    input_vector = vectorizer.transform([processed_input])

    similarities = cosine_similarity(input_vector, question_vectors)
    best_match = similarities.argmax()
    score = similarities[0][best_match]

    if score < 0.25:
        return "Sorry, I couldn't find a relevant answer. Please ask another question."

    return faq_data[questions[best_match]]

user_question = st.text_input(
    "Ask your question:",
    placeholder="Example: What is NLP?"
)

if st.button("Ask Chatbot"):
    if user_question.strip():
        answer = get_answer(user_question)

        st.subheader("🤖 Chatbot Response")
        st.success(answer)
    else:
        st.warning("Please enter a question.")

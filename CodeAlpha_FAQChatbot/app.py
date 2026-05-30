import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("🤖 FAQ Chatbot")
st.write("Ask me anything!")

# FAQ dataset (you can change topic later if you want)
faq_questions = [
    "What is your name?",
    "What services do you provide?",
    "How can I contact support?",
    "What is AI?",
    "Do you offer internships?",
    "How to submit projects?",
    "Where are you located?"
]

faq_answers = [
    "I am an AI FAQ chatbot created for CodeAlpha internship.",
    "We provide AI, Web Development and Software solutions.",
    "You can contact support at services@codealpha.tech",
    "AI stands for Artificial Intelligence.",
    "Yes! CodeAlpha offers internship opportunities.",
    "Upload your project to GitHub and submit the form.",
    "We operate online worldwide."
]

# NLP Vectorizer
vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(faq_questions)

# User input
user_question = st.text_input("Ask your question:")

if st.button("Send"):
    if user_question == "":
        st.warning("Please enter a question")
    else:
        user_vector = vectorizer.transform([user_question])
        similarity = cosine_similarity(user_vector, faq_vectors)
        index = similarity.argmax()
        response = faq_answers[index]

        st.success("Bot:")
        st.write(response)
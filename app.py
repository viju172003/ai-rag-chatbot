import streamlit as st

# Simulated Endee database (vector-like storage)
documents = [
    "Java is a programming language",
    "Python is used for AI and Machine Learning",
    "Machine Learning is a subset of Artificial Intelligence",
    "Artificial Intelligence helps machines learn and think"
]

# Simulated vector search (Endee concept)
def search(query):
    query = query.lower()
    
    best_match = ""
    max_score = 0
    
    for doc in documents:
        score = 0
        for word in query.split():
            if word in doc.lower():
                score += 1
        
        if score > max_score:
            max_score = score
            best_match = doc

    if best_match:
        return best_match
    else:
        return "No relevant answer found"

# UI
st.title("AI Chatbot using RAG + Endee")

st.write("This chatbot retrieves answers using a vector database concept (Endee)")

query = st.text_input("Ask your question:")

if query:
    result = search(query)
    st.success(result)
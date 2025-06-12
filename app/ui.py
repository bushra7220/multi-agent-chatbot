import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from myutils.pdf_loader import load_and_chunk_pdf
from models.model_selector import get_llm
from agents.question_answer_agent import build_qa_agent
from agents.summary_agent import build_summary_agent
from agents.mcq_generator import build_mcq_agent
from config.config import PDF_PATH
from myutils.vectorestore import create_vectorstore

# Load chunks once and cache
@st.cache_data(show_spinner=False)
def load_chunks():
    return load_and_chunk_pdf(PDF_PATH)

# Helper to extract response text
def extract_text(response):
    if hasattr(response, "generations") and response.generations:
        return response.generations[0].text
    elif hasattr(response, "content"):
        return response.content
    elif isinstance(response, dict):
        return response.get("answer") or response.get("result") or response.get("output") or response.get("text") or str(response)
    else:
        return str(response)

def main():
    st.title("📘 Multi-Agent Chatbot")

    # Load PDF chunks once
    chunks = load_chunks()
    vectorestore = create_vectorstore(chunks=chunks)

    # Model selection
    model_choice = st.selectbox("Select Model", ["gpt-3.5", "gpt-4"])
    llm = get_llm(model_choice)

    # Task selection
    task = st.radio("Choose Options", ["Question Answering", "Summary", "Generate MCQs"])

    # 🔹 Question Answering
    if task == "Question Answering":
        question = st.text_input("Enter your question:")
        if st.button("Get Answer") and question.strip():
            try:
                agent = build_qa_agent(llm, vectorstore=vectorestore)
                response = agent.invoke({"input": question})
                answer_text = extract_text(response)
                st.markdown(f"**Answer:** {answer_text}")
            except Exception as e:
                st.error(f"❌ Error: {e}")

    # 🔹 Summary Generation
    elif task == "Summary":
        user_input = st.text_area("Enter text to summarize (or leave empty to use textbook):")
        if st.button("Generate Summary"):
            try:
                text_to_summarize = user_input.strip() or " ".join([doc.page_content for doc in chunks])
                agent = build_summary_agent(llm)
                response = agent.invoke({"text": text_to_summarize})
                summary_text = extract_text(response)
                st.markdown(f"**Summary:** {summary_text}")
            except Exception as e:
                st.error(f"❌ Error: {e}")

    # 🔹 MCQ Generation
    elif task == "Generate MCQs":
        user_input = st.text_area("Enter text to generate MCQs (or leave empty to use textbook):")
        if st.button("Generate MCQs"):
            try:
                text_for_mcqs = user_input.strip() or " ".join([doc.page_content for doc in chunks[:10]])
                agent = build_mcq_agent(llm)
                response = agent.invoke({"context": text_for_mcqs})
                mcq_text = extract_text(response)
                st.markdown(f"**MCQs:**\n\n{mcq_text}")
            except Exception as e:
                st.error(f"❌ Error: {e}")

if __name__ == "__main__":
    main()

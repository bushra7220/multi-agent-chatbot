from langchain.prompts import PromptTemplate

def qa_prompt():
    return PromptTemplate(
        input_variables=["context", "query"],
        template="""
You are an expert academic assistant. Use the context below to answer the question accurately and concisely.

Context:
{context}

Question:
{input}

Answer in 2-3 sentences only, unless otherwise necessary.
""".strip()
    )

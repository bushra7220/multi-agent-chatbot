from langchain.prompts import PromptTemplate

summary_prompt = PromptTemplate(
    input_variables=["text"],
    template="""
You are a helpful AI assistant. Read the educational text below and generate a concise and clear summary.

Text:
{text}

Summarize this in your own words in 4-6 bullet points.
""".strip()
)

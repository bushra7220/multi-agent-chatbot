from langchain.prompts import PromptTemplate

mcq_prompt = PromptTemplate(
    input_variables=["context"],
    template="""
You are a helpful assistant. Based on the context below, generate as many meaningful multiple choice questions as possible.

From the context provided below, generate as **many distinct multiple choice questions (MCQs)** as possible.
Each question should have 4 options labeled (a), (b), (c), and (d) on a new line.
After each question, clearly indicate the correct answer on a new line starting with "Answer:".

Context:
{context}

Format:
1. Question text?

(a) Option A  
(b) Option B  
(c) Option C  
(d) Option D  
Answer: Option C

Only return the questions and answers in the above format. Do not add explanations or extra commentary.
""".strip()
)

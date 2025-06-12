from langchain_openai import ChatOpenAI
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from prompts.qa_prompt import qa_prompt


def build_qa_agent(llm, vectorstore):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
    llm = ChatOpenAI(verbose=True, temperature=0)
    prompt = qa_prompt()
    document_chain = create_stuff_documents_chain(llm=llm, prompt=prompt)

    return create_retrieval_chain(
        retriever=retriever, combine_docs_chain=document_chain
    )

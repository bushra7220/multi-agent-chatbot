from langchain_openai import ChatOpenAI

def get_llm(model_name: str, temperature=0):
    if model_name == "gpt-3.5":
        return ChatOpenAI(model="gpt-3.5-turbo", temperature=temperature)
    elif model_name == "gpt-4":
        return ChatOpenAI(model="gpt-4", temperature=temperature)
    else:
        raise ValueError(f"Model {model_name} not supported.")
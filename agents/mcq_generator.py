from prompts.mcq_prompt import mcq_prompt

def build_mcq_agent(llm):
    return mcq_prompt | llm

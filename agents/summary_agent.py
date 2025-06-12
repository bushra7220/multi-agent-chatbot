from prompts.summary_prompt import summary_prompt

def build_summary_agent(llm):
    return summary_prompt | llm

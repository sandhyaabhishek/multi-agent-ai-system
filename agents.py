from langchain_community.llms import Ollama

llm = Ollama(model="llama3")

def research_agent(topic):

    prompt = f"""
You are a research agent.

Research the topic and provide key points.

Topic:
{topic}
"""

    return llm.invoke(prompt)


def writer_agent(topic, research):

    prompt = f"""
You are a writer agent.

Write a clear article based on this research.

Topic:
{topic}

Research:
{research}
"""

    return llm.invoke(prompt)


def reviewer_agent(article):

    prompt = f"""
You are a reviewer agent.

Improve the following article and correct mistakes.

Article:
{article}
"""

    return llm.invoke(prompt)
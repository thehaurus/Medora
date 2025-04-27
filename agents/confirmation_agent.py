from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import OpenAI

llm = OpenAI(temperature=0)

def ask_user_confirmation(suggestions, topic):
    print(f"\n{topic}\n")
    for idx, item in enumerate(suggestions, start=1):
        print(f"{idx}. {item}")
    confirmation = input("Are you satisfied with these suggestions? (Yes/No): ")
    return confirmation

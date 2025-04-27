from langchain_community.llms import OpenAI

llm = OpenAI(temperature=0.2)

def analyze_health_report(text):
    prompt = f"""
You are a health expert.
Given this health report text:\n{text}\n
Identify:
- Possible deficiencies
- Diseases
- Suggestions

Respond in a clear bullet-point format.
"""
    return llm.predict(prompt)

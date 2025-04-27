from langchain_community.llms import OpenAI

llm = OpenAI(temperature=0.3)

def suggest_medicines(analysis_summary, previous_meds=[]):
    avoid_text = f"\nAvoid suggesting these medicines: {', '.join(previous_meds)}." if previous_meds else ""
    
    prompt = f"""
Based on the health analysis:
{analysis_summary}
Suggest 3 medicines with estimated prices in USD.{avoid_text}
Format: Medicine - Use - Price
"""
    return llm.predict(prompt)

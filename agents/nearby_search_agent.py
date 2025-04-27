from langchain_community.llms import OpenAI

llm = OpenAI(temperature=0.3)

def find_nearby_places(location, search_type, previous_list=[]):
    avoid_text = f"\nAvoid previous suggestions: {', '.join(previous_list)}." if previous_list else ""
    
    prompt = f"""
You are a search assistant.
Find 3 {search_type} near {location}.{avoid_text}
Format: Name - Rating - Address
"""
    return llm.predict(prompt)

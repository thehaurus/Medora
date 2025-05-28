from langgraph.graph import StateGraph, END
from agents.ocr_agent import extract_text_from_image
from agents.health_analysis_agent import analyze_health_report
from agents.prescription_agent import suggest_medicines
from agents.nearby_search_agent import find_nearby_places
from agents.confirmation_agent import ask_user_confirmation
from utils.helpers import parse_medicines

class HealthState:
    image_path: str
    location: str
    extracted_text: str = ""
    analysis: str = ""
    medicines: list = []
    shops: list = []
    doctors: list = []
    retries: int = 0

# --- Define Nodes (Agents)

def ocr_node(state: HealthState):
    state.extracted_text = extract_text_from_image(state.image_path)
    return state

def analysis_node(state: HealthState):
    state.analysis = analyze_health_report(state.extracted_text)
    return state

def medicine_node(state: HealthState):
    prev_meds = [med.split("-")[0].strip() for med in state.medicines]
    suggestions = suggest_medicines(state.analysis, prev_meds)
    state.medicines = parse_medicines(suggestions)
    return state

def medicine_confirmation(state: HealthState):
    confirmation = ask_user_confirmation(state.medicines, "💊 Medicines Suggested")
    if confirmation.lower() == "yes":
        return "approved"
    else:
        state.retries += 1
        return "retry"

def shop_node(state: HealthState):
    prev_shops = [shop.split("-")[0].strip() for shop in state.shops]
    suggestions = find_nearby_places(state.location, "medical shop", prev_shops)
    state.shops = parse_medicines(suggestions)
    return state

# For Complete Code, Contact : thehaurusai@gmail.com

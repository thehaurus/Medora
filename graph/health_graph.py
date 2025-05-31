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



# For Complete Code, Contact : thehaurusai@gmail.com

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

def shop_confirmation(state: HealthState):
    confirmation = ask_user_confirmation(state.shops, "🏥 Medical Shops Nearby")
    if confirmation.lower() == "yes":
        return "approved"
    else:
        state.retries += 1
        return "retry"

def doctor_node(state: HealthState):
    prev_docs = [doc.split("-")[0].strip() for doc in state.doctors]
    suggestions = find_nearby_places(state.location, "doctor", prev_docs)
    state.doctors = parse_medicines(suggestions)
    return state

def doctor_confirmation(state: HealthState):
    confirmation = ask_user_confirmation(state.doctors, "👨‍⚕️ Doctors Nearby")
    if confirmation.lower() == "yes":
        return "approved"
    else:
        state.retries += 1
        return "retry"

# --- Graph Building

def build_graph():
    graph = StateGraph(HealthState)
    graph.add_node("OCR", ocr_node)
    graph.add_node("Analysis", analysis_node)
    graph.add_node("SuggestMedicines", medicine_node)
    graph.add_node("ConfirmMedicines", medicine_confirmation)
    graph.add_node("SuggestShops", shop_node)
    graph.add_node("ConfirmShops", shop_confirmation)
    graph.add_node("SuggestDoctors", doctor_node)
    graph.add_node("ConfirmDoctors", doctor_confirmation)

    # Define edges
    graph.set_entry_point("OCR")
    graph.add_edge("OCR", "Analysis")
    graph.add_edge("Analysis", "SuggestMedicines")
    graph.add_edge("SuggestMedicines", "ConfirmMedicines")
    graph.add_conditional_edges("ConfirmMedicines", {
        "approved": "SuggestShops",
        "retry": "SuggestMedicines",
    })
    graph.add_edge("SuggestShops", "ConfirmShops")
    graph.add_conditional_edges("ConfirmShops", {
        "approved": "SuggestDoctors",
        "retry": "SuggestShops",
    })
    graph.add_edge("SuggestDoctors", "ConfirmDoctors")
    graph.add_conditional_edges("ConfirmDoctors", {
        "approved": END,
        "retry": "SuggestDoctors",
    })
    return graph.compile()

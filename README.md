# 🏥 AI-Powered Healthcare Assistant (Multi-Agent System)

The AI-Powered Healthcare Assistant is an intelligent multi-agent system designed to revolutionize healthcare services by automating the interpretation of medical reports and guiding patients to the best treatments and experts available nearby.

At its core, the system uses a LangGraph-based multi-agent architecture where each agent performs a specific task in a coordinated, human-like decision flow — including confirmation checks, alternative suggestions, and retry logic — ensuring a truly agentic behavior similar to how a real human assistant would operate.

🎯 Ideal For

- Health tech startups
- Hospital management software
- Personal health apps
- Online pharmacies
- Telemedicine platforms
- Insurance companies
- Elderly care solutions

This project is a complete **Multi-Agent/Agentic AI system** built using **LangChain**, **LangGraph**, and **Streamlit**, which:

- 📝 Takes a **health report image** as input
- 📋 Identifies **Possible Deficiencies**, **Diseases**, and **Suggested Medicines**
- 💰 Provides **Estimated Price** for medicines
- 🏪 Finds the **Best Nearby Medical Shops**
- 👨‍⚕️ Recommends **Top-Rated Doctors** nearby
- ✅ **Takes confirmation** from users at each stage, providing **alternatives** if user is not satisfied (Real Agentic Behavior)

## 🧠 Tech Stack

- **LangChain** (LLM Chains)
- **LangGraph** (Multi-Agent Graph)
- **Streamlit** (Frontend)
- **OpenAI** / **Gemini** (for LLM responses)
- **OCR**: EasyOCR / Tesseract
- **Places API**: (Google Places or similar for shops/doctors)

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/healthcare_agentic_system.git
cd healthcare_agentic_system

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app/streamlit_app.py
```

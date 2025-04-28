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

## 📄 Sample Input

![image alt](https://github.com/imayushthakur/Medora/blob/main/health_2.PNG?raw=true)

## 📄 Sample Output

🩺 **Possible Deficiencies**  
- **Vitamin D Deficiency**: Common due to limited sun exposure, especially in urban settings.  
- **Iron Deficiency (Anemia)**: Potentially indicated by fatigue and pallor.  
- **Vitamin B12 Deficiency**: May lead to neurological symptoms and fatigue.  
- **Calcium Deficiency**: Can result in bone-related issues.  

🧬 **Potential Diseases**  
- **Type 2 Diabetes Mellitus**: Characterized by elevated blood glucose levels.  
- **Hypertension**: High blood pressure readings.  
- **Dyslipidemia**: Abnormal lipid profiles, including high LDL or triglycerides.  
- **Hypothyroidism**: Indicated by elevated TSH levels.  

💊 **Suggested Medicines**  
- **Vitamin D Supplement**: Cholecalciferol 60,000 IU once weekly.  
- **Iron Supplement**: Ferrous sulfate 325 mg daily.  
- **Vitamin B12 Supplement**: Methylcobalamin 1500 mcg daily.  
- **Calcium Supplement**: Calcium carbonate 500 mg twice daily.  
- **Antidiabetic Medication**: Metformin 500 mg twice daily.  
- **Antihypertensive**: Amlodipine 5 mg once daily.  
- **Lipid-lowering Agent**: Atorvastatin 10 mg once daily.  
- **Thyroid Hormone Replacement**: Levothyroxine 50 mcg once daily.  

> 📢 *Note*: Dosages are general recommendations. Always consult a healthcare professional before starting any medication.

💸 **Estimated Price for Medicines**  
- Vitamin D Supplement: ₹100–₹150 per strip.  
- Iron Supplement: ₹50–₹100 per strip.  
- Vitamin B12 Supplement: ₹100–₹200 per strip.  
- Calcium Supplement: ₹100–₹150 per strip.  
- Metformin: ₹30–₹60 per strip.  
- Amlodipine: ₹20–₹50 per strip.  
- Atorvastatin: ₹50–₹100 per strip.  
- Levothyroxine: ₹30–₹60 per strip.  

💰 **Total Estimated Monthly Cost**: Approximately ₹500–₹1,000.

🏥 **Best Nearby Medical Shops in Bengaluru**
- **Aster Pharmacy - Rajaji Nagar 80 FT Road**  
  ⭐ Rating: 4.9/5 (835 Reviews)  
  📍 Address: No: 21/6/5, Shop No: 1, 80 Feet Road, 6th Block, Rajaji Nagar  
  🕘 Hours: 7:00 AM - 11:00 PM  
  ☎️ Phone: 08069867190

- **Apollo Pharmacy - Sarjapur Road**  
  📍 Address: No 11/50/3, Shop No 3, JP Building, Bellandur Gate, Varthur Hobli  
  🕘 Hours: 7:00 AM - 11:00 PM  
  ☎️ Phone: +91 080 2574 7363

- **MedPlus Pharmacy - Rajaji Nagar**  
  📍 Address: 128, 10th A Main Rd, Shivanagar, Basaveshwar Nagar  
  ☎️ Phone: 080 2295 7608

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
git clone https://github.com/imayushthakur/Medora.git

# Install dependencies
pip install -r requirements.txt

cd streamlit_app

# Run the app
streamlit run app/streamlit_app.py
```

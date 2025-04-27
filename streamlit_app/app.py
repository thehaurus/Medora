import streamlit as st
from graph.health_graph import build_graph, HealthState

st.title("🩺 Health Report Analyzer (Multi-Agent AI)")

uploaded_image = st.file_uploader("Upload Health Report Image", type=["png", "jpg", "jpeg"])
location = st.text_input("Enter your location (City, State)")

if st.button("Analyze Report"):
    if uploaded_image and location:
        with open("temp_image.jpg", "wb") as f:
            f.write(uploaded_image.getbuffer())

        graph = build_graph()
        state = HealthState(image_path="temp_image.jpg", location=location)
        final_state = graph.invoke(state)
        
        st.success("✅ Analysis Completed!")
        st.write("**Health Analysis:**", final_state.analysis)
        st.write("**Medicines:**", final_state.medicines)
        st.write("**Medical Shops Nearby:**", final_state.shops)
        st.write("**Doctors Nearby:**", final_state.doctors)
    else:
        st.error("Please upload image and enter location.")

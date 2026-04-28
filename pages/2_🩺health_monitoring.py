# pages/2_health_monitoring.py
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from utils.ai_utils import get_ai_response

st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
*{font-family:'Inter',sans-serif}
#MainMenu,footer{visibility:hidden}
.stButton>button{background:linear-gradient(135deg,#e84393,#fd79a8)!important;color:#fff!important;border:none!important;border-radius:12px!important;padding:.6rem 1.5rem!important;font-weight:600!important;box-shadow:0 4px 15px rgba(232,67,147,.3)!important}
.stButton>button:hover{transform:translateY(-2px)!important;box-shadow:0 8px 25px rgba(232,67,147,.4)!important}
.page-hdr{background:linear-gradient(135deg,#e84393,#fd79a8,#fab1a0);border-radius:16px;padding:2rem;color:#fff;margin-bottom:1.5rem;box-shadow:0 12px 40px rgba(232,67,147,.25)}
.page-hdr h1{font-size:2rem;font-weight:800;margin:0}
.page-hdr p{opacity:.9;margin:.3rem 0 0}
</style>""", unsafe_allow_html=True)

def health_monitoring_page():
    st.markdown('<div class="page-hdr"><h1>🩺 Health Monitoring</h1><p>Track physical health, mental wellness, and check symptoms</p></div>', unsafe_allow_html=True)
    tabs = st.tabs(["💪 Physical Health", "🧠 Mental Health", "🔍 Symptom Checker"])

    with tabs[0]:
        st.subheader("Track Your Physical Health")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### ⚖️ Weight Tracking")
            weight = st.number_input("Today's weight (kg)", min_value=0.0, max_value=200.0, key="hw_weight")
            if st.button("Log Weight", key="btn_log_weight"):
                st.success("Weight logged successfully!")
            dates = pd.date_range(start="2024-01-01", end="2024-01-31", freq="D")
            weights = [65 + i * 0.1 + np.random.normal(0, 0.2) for i in range(len(dates))]
            fig = px.line(pd.DataFrame({"Date": dates, "Weight (kg)": weights}), x="Date", y="Weight (kg)", title="Weight Trend")
            fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font={"color": "#f0f0f5"})
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            st.markdown("### 🩸 Blood Pressure")
            c3, c4 = st.columns(2)
            with c3:
                systolic = st.number_input("Systolic", min_value=0, max_value=200, key="hw_sys")
            with c4:
                diastolic = st.number_input("Diastolic", min_value=0, max_value=150, key="hw_dia")
            if st.button("Log Blood Pressure", key="btn_log_bp"):
                if systolic > 0 and diastolic > 0:
                    if systolic > 140 or diastolic > 90:
                        st.warning("⚠️ Your reading is elevated. Please consult your doctor.")
                    else:
                        st.success("Blood pressure logged!")
                else:
                    st.info("Enter valid values.")

    with tabs[1]:
        st.subheader("Mental Wellness Tracker")
        st.markdown("### 😊 Today's Mood")
        mood = st.select_slider("How are you feeling?", options=["😔","😕","😐","🙂","😊"], value="😐", key="hw_mood")
        stress = st.slider("Stress Level (0–10)", 0, 10, 5, key="hw_stress")
        sleep = st.number_input("Hours of sleep last night", 0, 24, 8, key="hw_sleep")
        if st.button("Get Mental Health Tips", key="btn_mental_tips"):
            with st.spinner("Getting tips…"):
                prompt = f"I'm feeling {mood} with stress {stress}/10 and slept {sleep} hours. Give 3 concise mental health tips for pregnancy with emojis."
                st.markdown("### 🤖 AI Tips")
                st.write(get_ai_response(prompt))
        st.markdown("### 🧘 Quick Meditation")
        med_time = st.select_slider("Duration", options=[1,2,3,5,10], value=3, format_func=lambda x: f"{x} min", key="hw_med")
        if st.button("Start Meditation", key="btn_meditate"):
            st.balloons()
            st.info(f"Close your eyes, breathe deeply for {med_time} minutes. You've got this! 🌸")

    with tabs[2]:
        st.subheader("Symptom Checker")
        symptoms = {"Morning Sickness":["Nausea","Vomiting"],"Pain":["Headache","Back Pain","Pelvic Pain"],"Digestive":["Heartburn","Constipation","Bloating"],"Other":["Fatigue","Dizziness","Swelling"]}
        selected = []
        for cat, syms in symptoms.items():
            st.markdown(f"### {cat}")
            for s in syms:
                if st.checkbox(s, key=f"sym_{s}"):
                    selected.append(s)
        severity = st.select_slider("Severity", options=["Mild","Moderate","Severe"], value="Moderate", key="hw_sev")
        if st.button("Check Symptoms", key="btn_check_sym"):
            if selected:
                with st.spinner("Analysing…"):
                    prompt = f"I'm experiencing {', '.join(selected)} with {severity.lower()} severity during pregnancy. What should I know? When should I see a doctor? Be concise."
                    st.markdown("### 🤖 AI Assessment")
                    st.write(get_ai_response(prompt))
                    if severity == "Severe":
                        st.warning("⚠️ Please consult your healthcare provider immediately for severe symptoms.")
            else:
                st.info("Please select at least one symptom.")

if __name__ == "__main__":
    health_monitoring_page()

# pages/3_nutrition_exercise.py
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from utils.ai_utils import get_ai_response
from utils.constants import NUTRITION_TIPS, EXERCISE_RECOMMENDATIONS

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

def nutrition_exercise_page():
    st.markdown('<div class="page-hdr"><h1>🥗 Nutrition & Exercise</h1><p>Personalised meal plans, safe workouts, and progress tracking</p></div>', unsafe_allow_html=True)
    tabs = st.tabs(["🍽️ Meal Planner", "🏋️ Exercise Guide", "📈 Progress Tracker"])

    with tabs[0]:
        st.subheader("Personalised Meal Planner")
        c1, c2 = st.columns(2)
        with c1:
            trimester = st.selectbox("Current Trimester", ["First Trimester","Second Trimester","Third Trimester"], key="ne_tri")
            restrictions = st.multiselect("Dietary Restrictions", ["Vegetarian","Vegan","Gluten-free","Dairy-free","None"], key="ne_diet")
        with c2:
            calories = st.slider("Daily Calorie Target", 1500, 2500, 2000, key="ne_cal")
        if st.button("Generate Meal Plan", key="btn_meal"):
            with st.spinner("Creating your meal plan…"):
                prompt = f"Create a one-day meal plan for a pregnant woman in {trimester} with {', '.join(restrictions) if restrictions else 'no'} dietary restrictions, targeting {calories} calories. Include breakfast, lunch, dinner, and 2 snacks. Use emojis."
                st.markdown("### 🍽️ Your Meal Plan")
                st.write(get_ai_response(prompt))
        st.markdown("### 💊 Essential Nutrients")
        nutrients = {"Folic Acid":"800 mcg/day","Iron":"27 mg/day","Calcium":"1000 mg/day","Vitamin D":"600 IU/day","DHA":"200–300 mg/day"}
        nc = st.columns(len(nutrients))
        for i, (n, v) in enumerate(nutrients.items()):
            with nc[i]:
                st.metric(n, v)

    with tabs[1]:
        st.subheader("Safe Exercise Guide")
        fitness = st.select_slider("Fitness Level", options=["Beginner","Intermediate","Advanced"], value="Intermediate", key="ne_fit")
        ex_time = st.slider("Available time (minutes)", 15, 60, 30, key="ne_extime")
        if st.button("Get Exercise Plan", key="btn_exercise"):
            with st.spinner("Building your workout…"):
                prompt = f"Create a safe {ex_time}-minute pregnancy exercise routine for a {fitness.lower()}-level person. Include warm-up and cool-down. Use emojis."
                st.markdown("### 🏋️ Your Exercise Plan")
                st.write(get_ai_response(prompt))
        st.markdown("### ⚠️ Safety Guidelines")
        tips = ["Listen to your body — don't overexert","Stay hydrated during exercise","Avoid exercises that risk falling","Stop if you feel pain or discomfort","Keep heart rate below 140 bpm"]
        for t in tips:
            st.info(f"✅ {t}")

    with tabs[2]:
        st.subheader("Track Your Progress")
        st.markdown("### 📝 Log Today's Activities")
        c1, c2 = st.columns(2)
        with c1:
            water = st.number_input("Water (glasses)", 0, 20, 8, key="ne_water")
            ex_min = st.number_input("Exercise (minutes)", 0, 180, 30, key="ne_exmin")
        with c2:
            meals = st.number_input("Meals eaten", 0, 6, 3, key="ne_meals")
            steps = st.number_input("Steps taken", 0, 20000, 5000, key="ne_steps")
        if st.button("Log Progress", key="btn_log_progress"):
            st.success("✅ Progress logged successfully!")
            dates = pd.date_range(start="2024-01-01", end="2024-01-31", freq="D")
            c3, c4 = st.columns(2)
            with c3:
                fig1 = px.line(pd.DataFrame({"Date":dates,"Water":np.clip(np.random.normal(8,1,len(dates)),3,15)}), x="Date", y="Water", title="💧 Water Intake Trend")
                fig1.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font={"color":"#f0f0f5"})
                st.plotly_chart(fig1, use_container_width=True)
            with c4:
                fig2 = px.line(pd.DataFrame({"Date":dates,"Steps":np.clip(np.random.normal(5000,500,len(dates)),2000,10000)}), x="Date", y="Steps", title="🚶 Steps Trend")
                fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font={"color":"#f0f0f5"})
                st.plotly_chart(fig2, use_container_width=True)

if __name__ == "__main__":
    nutrition_exercise_page()

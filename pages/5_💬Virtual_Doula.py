# pages/5_virtual_doula.py
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
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

def virtual_doula_page():
    st.markdown('<div class="page-hdr"><h1>👩‍⚕️ Virtual Doula</h1><p>Birth planning, labour preparation, and postpartum care guidance</p></div>', unsafe_allow_html=True)
    tabs = st.tabs(["📋 Birth Plan", "🏥 Labour Prep", "🌸 Postpartum Care"])

    # ── Birth Plan ──────────────────────────────────────
    with tabs[0]:
        st.subheader("Create Your Birth Plan")
        prefs = {
            "Birth Environment": st.multiselect("Preferred environment", ["Hospital","Birth Center","Home Birth"], key="vd_env"),
            "Pain Management": st.multiselect("Pain management", ["Natural","Epidural","Nitrous Oxide","Hydrotherapy"], key="vd_pain"),
            "Support Team": st.multiselect("Who should be present?", ["Partner","Doula","Family Member","Midwife"], key="vd_team"),
            "Interventions": st.multiselect("Intervention preference", ["Only if medically necessary","Prefer to avoid","Open to all options"], key="vd_interv"),
        }
        if st.button("Generate Birth Plan", key="btn_birth_plan"):
            with st.spinner("Creating your plan…"):
                prompt = f"Create a detailed, well-formatted birth plan:\nEnvironment: {', '.join(prefs['Birth Environment']) or 'Not specified'}\nPain: {', '.join(prefs['Pain Management']) or 'Not specified'}\nSupport: {', '.join(prefs['Support Team']) or 'Not specified'}\nInterventions: {', '.join(prefs['Interventions']) or 'Not specified'}"
                plan = get_ai_response(prompt)
                st.session_state.vd_birth_plan = plan
                st.markdown("### 📋 Your Birth Plan")
                st.write(plan)

        # Download button (outside the generate button)
        if "vd_birth_plan" in st.session_state and st.session_state.vd_birth_plan:
            st.download_button(
                "📥 Download Birth Plan (.txt)",
                st.session_state.vd_birth_plan,
                file_name="birth_plan.txt",
                mime="text/plain",
                key="btn_download_plan",
            )

    # ── Labour Prep ─────────────────────────────────────
    with tabs[1]:
        st.subheader("Labour Preparation Guide")
        st.markdown("### ⏱️ Contraction Timer")
        c1, c2 = st.columns(2)
        with c1:
            if st.button("▶️ Start Contraction", key="btn_start_con"):
                st.session_state.contraction_start = datetime.now()
                st.info("⏱️ Timing contraction…")
            if st.button("⏹️ End Contraction", key="btn_end_con"):
                if "contraction_start" in st.session_state:
                    dur = (datetime.now() - st.session_state.contraction_start).seconds
                    if "contractions" not in st.session_state:
                        st.session_state.contractions = []
                    st.session_state.contractions.append({"time": datetime.now(), "duration": dur})
                    st.success(f"Contraction recorded: {dur} seconds")
                else:
                    st.warning("Press Start first!")
        with c2:
            if "contractions" in st.session_state and st.session_state.contractions:
                df = pd.DataFrame(st.session_state.contractions)
                fig = px.line(df, x="time", y="duration", title="Contraction Pattern", markers=True)
                fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font={"color": "#f0f0f5"})
                st.plotly_chart(fig, use_container_width=True)

        st.markdown("### 🧘 Labour Positions")
        positions = {"Early Labour":["Walking","Resting","Gentle Swaying"],"Active Labour":["Birth Ball","Squatting","Hands and Knees"],"Transition":["Supported Squat","Side-Lying","Leaning Forward"]}
        stage = st.selectbox("Select Labour Stage", list(positions.keys()), key="vd_stage")
        for p in positions[stage]:
            st.markdown(f"- {p}")
        if st.button("Get Position Tips", key="btn_pos_tips"):
            with st.spinner("Getting tips…"):
                st.write(get_ai_response(f"Provide detailed instructions for {stage} positions: {', '.join(positions[stage])}. Be concise with emojis."))

    # ── Postpartum Care ─────────────────────────────────
    with tabs[2]:
        st.subheader("Postpartum Recovery & Care")
        st.markdown("### 📅 Recovery Timeline")
        weeks = st.slider("Weeks Postpartum", 0, 12, 0, key="vd_pp_weeks")
        if st.button("Get Recovery Info", key="btn_recovery"):
            with st.spinner("Getting info…"):
                st.write(get_ai_response(f"What should a new mother expect during week {weeks} postpartum? Include physical, emotional, and baby care tips. Be concise with emojis."))

        st.markdown("### ✅ Daily Self-Care Checklist")
        items = ["Rested for at least 2 hours","Eaten 3 nutritious meals","Taken prescribed vitamins","Done basic hygiene routine","Had support person help","Moved body gently / stretched","Connected with another adult","Hydrated well (8+ glasses)"]
        done = []
        for item in items:
            if st.checkbox(item, key=f"sc_{item}"):
                done.append(item)
        pct = len(done) / len(items)
        st.progress(pct)
        if pct == 1.0:
            st.balloons()
            st.success("🎉 Amazing! You completed all self-care tasks!")
        else:
            st.write(f"Completed **{int(pct * 100)}%** of your self-care tasks today")

        st.markdown("### 😊 Mood Tracker")
        mood = st.select_slider("How are you feeling?", options=["😔","😕","😐","🙂","😊"], key="vd_mood")
        if mood in ["😔", "😕"]:
            st.warning("💛 It's normal to have ups and downs. Please talk to your healthcare provider if you feel down frequently.")
            if st.button("Get Support Resources", key="btn_pp_support"):
                with st.spinner("Finding resources…"):
                    st.write(get_ai_response("Provide resources and coping strategies for postpartum mood concerns. Be supportive and concise with emojis."))

if __name__ == "__main__":
    virtual_doula_page()

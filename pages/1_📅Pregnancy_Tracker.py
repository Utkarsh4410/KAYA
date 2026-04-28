# pages/1_pregnancy_tracker.py
import streamlit as st
import plotly.graph_objects as go
from datetime import datetime, timedelta
from utils.constants import PREGNANCY_WEEKS
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

def calculate_due_date(lp):
    return lp + timedelta(days=280)

def calculate_current_week(lp):
    days = (datetime.now().date() - lp).days
    return min(max(1, days // 7), 40)

def pregnancy_tracker_page():
    st.markdown('<div class="page-hdr"><h1>📅 Pregnancy Tracker</h1><p>Track your pregnancy week by week with AI-powered insights</p></div>', unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    with col1:
        last_period = st.date_input("First day of your last period?", datetime.now().date() - timedelta(weeks=12), key="tracker_lp")
        cw = calculate_current_week(last_period)
        dd = calculate_due_date(last_period)
        st.progress(cw / 40)
        tri = "First Trimester" if cw <= 13 else ("Second Trimester" if cw <= 26 else "Third Trimester")
        st.markdown(f"### Week {cw} of 40 &nbsp;·&nbsp; {tri}")
        fig = go.Figure(go.Indicator(mode="gauge+number", value=cw, title={"text":"Weeks"}, domain={"x":[0,1],"y":[0,1]}, gauge={"axis":{"range":[0,40]},"bar":{"color":"#e84393"},"steps":[{"range":[0,13],"color":"rgba(232,67,147,.15)"},{"range":[13,26],"color":"rgba(232,67,147,.25)"},{"range":[26,40],"color":"rgba(232,67,147,.35)"}]}))
        fig.update_layout(height=280, paper_bgcolor="rgba(0,0,0,0)", font={"color":"#f0f0f5"})
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.markdown("### 🍼 Your Baby This Week")
        closest = max((w for w in PREGNANCY_WEEKS if w <= cw), default=1)
        st.info(PREGNANCY_WEEKS[closest])
        st.markdown("### 📅 Due Date")
        st.success(f"🎉 {dd.strftime('%B %d, %Y')}")
        st.markdown("### 🤖 AI Insights")
        if st.button("Get Personalised Insights", key="btn_insights"):
            with st.spinner("Generating…"):
                st.write(get_ai_response(f"What should a pregnant woman expect during week {cw}? Give 3 concise tips with emojis."))
    st.markdown("---")
    st.markdown("### 🏁 Pregnancy Milestones")
    tl = {"First Trimester (1–13)":["First prenatal visit","First ultrasound","Morning sickness subsides","Embryonic period ends"],"Second Trimester (14–26)":["Gender reveal possible","Baby's first movements","Anatomy scan (20 wks)","Glucose screening"],"Third Trimester (27–40)":["Baby shower","Create birth plan","Pack hospital bag","Begin maternity leave"]}
    for label, ms in tl.items():
        with st.expander(label):
            for m in ms:
                st.checkbox(m, key=f"ms_{m}")

if __name__ == "__main__":
    pregnancy_tracker_page()

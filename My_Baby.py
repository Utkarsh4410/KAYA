import streamlit as st
from datetime import datetime

# ── Page configuration ──────────────────────────────────────────────
st.set_page_config(
    page_title="Kaya — AI Pregnancy Assistant",
    page_icon="👶",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Premium CSS Theme ───────────────────────────────────────────────
st.markdown("""
<style>
/* ── Google Font ─────────────────────────────────────── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

* { font-family: 'Inter', sans-serif; }

/* ── Hide Streamlit defaults ─────────────────────────── */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* ── Gradient Hero Banner ────────────────────────────── */
.hero-banner {
    background: linear-gradient(135deg, #e84393 0%, #fd79a8 40%, #fab1a0 100%);
    border-radius: 20px;
    padding: 3rem 2.5rem;
    margin-bottom: 2rem;
    color: white;
    position: relative;
    overflow: hidden;
    box-shadow: 0 20px 60px rgba(232, 67, 147, 0.3);
}
.hero-banner h1 {
    font-size: 2.8rem;
    font-weight: 800;
    margin: 0 0 0.5rem 0;
    letter-spacing: -1px;
}
.hero-banner p {
    font-size: 1.15rem;
    opacity: 0.92;
    margin: 0;
    font-weight: 300;
}
.hero-banner::after {
    content: '';
    position: absolute;
    top: -50%;
    right: -20%;
    width: 400px;
    height: 400px;
    background: rgba(255,255,255,0.08);
    border-radius: 50%;
}

/* ── Stat Cards ──────────────────────────────────────── */
div[data-testid="stMetric"] {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    border: 1px solid rgba(232, 67, 147, 0.25);
    border-radius: 16px;
    padding: 1.2rem 1rem;
    box-shadow: 0 8px 32px rgba(0,0,0,0.2);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
div[data-testid="stMetric"]:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 40px rgba(232, 67, 147, 0.2);
}
div[data-testid="stMetric"] label {
    color: #fd79a8 !important;
    font-weight: 600;
    text-transform: uppercase;
    font-size: 0.75rem;
    letter-spacing: 1px;
}
div[data-testid="stMetric"] [data-testid="stMetricValue"] {
    color: #ffffff !important;
    font-weight: 700;
}

/* ── Feature Cards ───────────────────────────────────── */
.feature-card {
    background: linear-gradient(145deg, #1a1a2e 0%, #16213e 100%);
    border: 1px solid rgba(232, 67, 147, 0.15);
    border-radius: 16px;
    padding: 1.8rem;
    margin-bottom: 1rem;
    transition: all 0.3s ease;
    min-height: 160px;
}
.feature-card:hover {
    border-color: rgba(232, 67, 147, 0.5);
    transform: translateY(-2px);
    box-shadow: 0 8px 30px rgba(232, 67, 147, 0.15);
}
.feature-card h3 {
    color: #fd79a8;
    margin: 0 0 0.5rem 0;
    font-weight: 700;
}
.feature-card p {
    color: #b0b0c0;
    font-size: 0.95rem;
    line-height: 1.5;
}

/* ── Buttons ─────────────────────────────────────────── */
.stButton > button {
    background: linear-gradient(135deg, #e84393, #fd79a8) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.6rem 1.5rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.3px;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px rgba(232, 67, 147, 0.3) !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(232, 67, 147, 0.4) !important;
}

/* ── Sidebar ─────────────────────────────────────────── */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d0d1a 0%, #1a1a2e 100%);
    border-right: 1px solid rgba(232, 67, 147, 0.15);
}
section[data-testid="stSidebar"] .stImage {
    border-radius: 16px;
    overflow: hidden;
}

/* ── Expander ────────────────────────────────────────── */
.streamlit-expanderHeader {
    background: rgba(232, 67, 147, 0.08) !important;
    border-radius: 12px !important;
    font-weight: 600;
}

/* ── Info/Tip Cards ──────────────────────────────────── */
.stAlert {
    border-radius: 12px !important;
    border-left: 4px solid #e84393 !important;
}

/* ── Section Header ──────────────────────────────────── */
.section-header {
    font-size: 1.5rem;
    font-weight: 700;
    color: #f0f0f5;
    margin: 2rem 0 1rem 0;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid rgba(232, 67, 147, 0.3);
}

/* ── Footer ──────────────────────────────────────────── */
.kaya-footer {
    text-align: center;
    color: #666;
    padding: 2rem 0 1rem 0;
    font-size: 0.85rem;
    border-top: 1px solid rgba(232, 67, 147, 0.15);
    margin-top: 3rem;
}
.kaya-footer a {
    color: #e84393;
    text-decoration: none;
}
</style>
""", unsafe_allow_html=True)


def main():
    # ── Sidebar ─────────────────────────────────────────
    with st.sidebar:
        st.image("images/MY BABY.png", use_container_width=True)
        st.markdown("---")
        st.markdown("### 🔗 Quick Links")
        st.page_link("My_Baby.py", label="🏠 Home", icon=None)
        st.page_link("pages/1_📅Pregnancy_Tracker.py", label="📅 Pregnancy Tracker")
        st.page_link("pages/2_🩺health_monitoring.py", label="🩺 Health Monitor")
        st.page_link("pages/3_🥗Nutrition_Exercise.py", label="🥗 Nutrition & Exercise")
        st.page_link("pages/4_🎙️voice_assistant.py", label="🎙️ Voice Assistant")
        st.page_link("pages/5_💬Virtual_Doula.py", label="💬 Virtual Doula")
        st.markdown("---")
        st.markdown(
            "<p style='text-align:center; color:#888; font-size:0.75rem;'>"
            "Powered by Groq AI</p>",
            unsafe_allow_html=True,
        )

    # ── Hero Banner ─────────────────────────────────────
    st.markdown("""
    <div class="hero-banner">
        <h1>Welcome to Kaya 👶</h1>
        <p>Your AI-Powered Pregnancy Journey Companion — personalised guidance, health monitoring, and expert support at every step.</p>
    </div>
    """, unsafe_allow_html=True)

    # ── Quick Stats ─────────────────────────────────────
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Active Users", value="100K+", delta="↑ 15%")
    with col2:
        st.metric(label="Success Stories", value="50K+", delta="↑ 12%")
    with col3:
        st.metric(label="Expert Doctors", value="1,000+", delta="↑ 5%")

    # ── Key Features ────────────────────────────────────
    st.markdown('<div class="section-header">✨ Key Features</div>', unsafe_allow_html=True)

    f1, f2 = st.columns(2)
    with f1:
        st.markdown("""
        <div class="feature-card">
            <h3>🌟 Smart Tracking</h3>
            <p>AI-powered pregnancy tracking with week-by-week insights, baby size visualisation, and milestone notifications.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="feature-card">
            <h3>👩‍⚕️ Virtual Doula</h3>
            <p>24/7 AI-powered pregnancy support — birth plans, labour preparation, and postpartum care guidance.</p>
        </div>
        """, unsafe_allow_html=True)

    with f2:
        st.markdown("""
        <div class="feature-card">
            <h3>📊 Health Monitor</h3>
            <p>Comprehensive health monitoring with weight tracking, blood pressure logging, mood tracking, and symptom checker.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="feature-card">
            <h3>🥗 Nutrition & Exercise</h3>
            <p>Personalised meal plans, safe exercise routines, and progress tracking tailored to your trimester.</p>
        </div>
        """, unsafe_allow_html=True)

    # ── What's New ──────────────────────────────────────
    st.markdown('<div class="section-header">🆕 Recent Updates</div>', unsafe_allow_html=True)
    with st.expander("What's New", expanded=True):
        st.markdown("""
        - 🎉 **New Feature**: Advanced baby size visualisation for all 40 weeks
        - 🎙️ **Voice Assistant**: Chat with AI using text or quick phrases with text-to-speech
        - 🩺 **Health Monitor**: Enhanced symptom checker with AI-powered assessments
        - 📊 **Progress Tracker**: Water intake, steps, and exercise logging with trend charts
        """)

    # ── Today's Tips ────────────────────────────────────
    st.markdown('<div class="section-header">💡 Today\'s Tips</div>', unsafe_allow_html=True)
    t1, t2 = st.columns(2)
    with t1:
        st.info("💧 Stay hydrated! Aim for 8–10 glasses of water daily.")
    with t2:
        st.info("🧘‍♀️ Take short walks to maintain good circulation and reduce swelling.")

    # ── Community ───────────────────────────────────────
    st.markdown('<div class="section-header">🤝 Community Highlights</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("#### 👥 Active Members")
        st.write("Join our growing community of mothers.")
        st.button("Join Community", key="btn_community")
    with c2:
        st.markdown("#### 📅 Upcoming Events")
        st.write("Check our latest webinars and events.")
        st.button("View Events", key="btn_events")
    with c3:
        st.markdown("#### 💬 Support Group")
        st.write("Connect with other parents for support.")
        st.button("Join Group", key="btn_group")

    # ── Footer ──────────────────────────────────────────
    st.markdown("---")
    f1, f2, f3 = st.columns(3)
    with f1:
        st.markdown("#### 📧 Contact Us")
        st.write("support@kaya.ai")
    with f2:
        st.markdown("#### 🔗 Follow Us")
        st.write("GitHub · Twitter · Instagram")
    with f3:
        st.markdown("#### ❓ Help & Support")
        st.button("Get Help", key="btn_help")

    st.markdown(
        f"<div class='kaya-footer'>© {datetime.now().year} Kaya. "
        "All rights reserved. Made with ❤️ for mothers everywhere.</div>",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()

# pages/4_voice_assistant.py
import streamlit as st
import os
import tempfile
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
.chat-user{background:rgba(232,67,147,.12);border-radius:12px;padding:1rem;margin:.5rem 0;border-left:4px solid #e84393}
.chat-bot{background:rgba(26,26,46,.8);border-radius:12px;padding:1rem;margin:.5rem 0;border-left:4px solid #fd79a8}
</style>""", unsafe_allow_html=True)

# Optional TTS
try:
    from gtts import gTTS
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False

def speak(text):
    """Convert text to speech and return the audio file path."""
    if not TTS_AVAILABLE:
        return None
    try:
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        gTTS(text, lang="en", slow=False).save(tmp.name)
        return tmp.name
    except Exception:
        return None

def voice_assistant_page():
    st.markdown('<div class="page-hdr"><h1>🎙️ AI Chat Assistant</h1><p>Ask anything about pregnancy — get instant AI-powered answers with optional text-to-speech</p></div>', unsafe_allow_html=True)

    # Init session state
    if "va_messages" not in st.session_state:
        st.session_state.va_messages = []
    if "va_tts" not in st.session_state:
        st.session_state.va_tts = True

    # Settings
    col_set1, col_set2 = st.columns([3, 1])
    with col_set2:
        if TTS_AVAILABLE:
            st.session_state.va_tts = st.toggle("🔊 Read aloud", value=st.session_state.va_tts, key="tts_toggle")

    # Display conversation history
    for msg in st.session_state.va_messages:
        if msg["role"] == "user":
            st.markdown(f'<div class="chat-user"><strong>You:</strong> {msg["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-bot"><strong>Kaya:</strong> {msg["content"]}</div>', unsafe_allow_html=True)

    # Quick phrases
    st.markdown("### ⚡ Quick Questions")
    qc1, qc2, qc3, qc4 = st.columns(4)
    quick_phrases = {
        "qp1": ("🤰 Pregnancy tips", "Give me 3 quick pregnancy wellness tips with emojis."),
        "qp2": ("🥗 Nutrition advice", "What are the top 3 foods I should eat during pregnancy? Be concise."),
        "qp3": ("😴 Sleep help", "How can I sleep better during pregnancy? Give 3 tips with emojis."),
        "qp4": ("🧘 Relaxation", "Suggest a 5-minute relaxation exercise for a pregnant woman. Be concise."),
    }
    cols = [qc1, qc2, qc3, qc4]
    for i, (key, (label, prompt)) in enumerate(quick_phrases.items()):
        with cols[i]:
            if st.button(label, key=f"btn_{key}"):
                st.session_state.va_messages.append({"role": "user", "content": label})
                with st.spinner("Thinking…"):
                    resp = get_ai_response(f"You are Kaya, a friendly pregnancy assistant. {prompt}")
                st.session_state.va_messages.append({"role": "assistant", "content": resp})
                if st.session_state.va_tts:
                    audio_path = speak(resp)
                    if audio_path:
                        st.audio(audio_path)
                        os.unlink(audio_path)
                st.rerun()

    # Chat input
    st.markdown("### 💬 Ask Kaya Anything")
    user_input = st.chat_input("Type your question here…", key="va_chat_input")
    if user_input:
        st.session_state.va_messages.append({"role": "user", "content": user_input})
        # Build context from last 4 messages
        ctx = "\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.va_messages[-4:]])
        with st.spinner("Thinking…"):
            resp = get_ai_response(f"You are Kaya, a friendly pregnancy assistant. Context:\n{ctx}\n\nUser: {user_input}\nRespond helpfully and concisely.")
        st.session_state.va_messages.append({"role": "assistant", "content": resp})
        if st.session_state.va_tts:
            audio_path = speak(resp)
            if audio_path:
                st.audio(audio_path)
                os.unlink(audio_path)
        st.rerun()

    # Clear chat
    if st.session_state.va_messages:
        if st.button("🗑️ Clear Chat", key="btn_clear_chat"):
            st.session_state.va_messages = []
            st.rerun()

if __name__ == "__main__":
    voice_assistant_page()

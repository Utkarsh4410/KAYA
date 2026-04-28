# Kaya — AI Pregnancy Assistant 👶

<p align="center">
    <img src="images/MY BABY.png" alt="Kaya Logo" width="200"/>
</p>

<p align="center">
    <a href="https://www.python.org/downloads/">
        <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version"/>
    </a>
    <a href="https://streamlit.io">
        <img src="https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/>
    </a>
    <a href="https://console.groq.com">
        <img src="https://img.shields.io/badge/Groq-LLaMA_3.3-orange?style=for-the-badge" alt="Groq AI"/>
    </a>
</p>

<p align="center">
    <a href="#-features">Features</a>
    ·
    <a href="#-quick-start">Quick Start</a>
    ·
    <a href="#-tech-stack">Tech Stack</a>
    ·
    <a href="#-contributing">Contributing</a>
</p>

## 🌟 Overview

**Kaya** is a comprehensive AI-powered web application designed to support mothers throughout their pregnancy journey. Built with Streamlit and powered by **Groq's LLaMA 3.3** model, it offers personalised guidance, health monitoring, and essential pregnancy-related information at your fingertips.

## ✨ Features

<details>
<summary>📅 Pregnancy Tracker</summary>
<br>
• Week-by-week development tracking (all 40 weeks)<br>
• Interactive pregnancy progress gauge<br>
• Baby size visualisation with fruit comparisons<br>
• AI-powered personalised insights<br>
• Milestone timeline with checklists
</details>

<details>
<summary>🩺 Health Monitoring</summary>
<br>
• Weight tracking with trend charts<br>
• Blood pressure logging with alerts<br>
• Mental health assessment & AI tips<br>
• Mood and stress tracking<br>
• Symptom checker with AI assessment
</details>

<details>
<summary>🥗 Nutrition & Exercise</summary>
<br>
• AI-generated personalised meal plans<br>
• Trimester-specific nutritional guidance<br>
• Safe exercise routines by fitness level<br>
• Progress tracking (water, steps, meals)
</details>

<details>
<summary>🎙️ AI Chat Assistant</summary>
<br>
• Text-based chat with Kaya AI<br>
• Quick-question buttons for common topics<br>
• Optional text-to-speech responses<br>
• Conversation history
</details>

<details>
<summary>👩‍⚕️ Virtual Doula</summary>
<br>
• AI-generated birth plan creator<br>
• Contraction timer with pattern tracking<br>
• Labour position recommendations<br>
• Postpartum recovery timeline<br>
• Daily self-care checklist & mood tracker
</details>

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- A free [Groq API key](https://console.groq.com/keys)

### Installation

```bash
# Clone the repository
git clone https://github.com/Utkarsh4410/KAYA.git
cd KAYA

# Create virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Set up your API key
cp .env.example .env
# Edit .env and add your GROQ_API_KEY
```

### Run

```bash
streamlit run My_Baby.py
```

The app will open at `http://localhost:8501`.

## 💻 Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | Streamlit |
| **AI Model** | LLaMA 3.3 70B (via Groq) |
| **Speech** | Whisper V3, Google TTS |
| **Charts** | Plotly |
| **Data** | Pandas, NumPy |
| **Language** | Python 3.8+ |

## 📁 Project Structure

```
KAYA/
├── My_Baby.py                  # Main app (home page)
├── pages/
│   ├── 1_📅Pregnancy_Tracker.py
│   ├── 2_🩺health_monitoring.py
│   ├── 3_🥗Nutrition_Exercise.py
│   ├── 4_🎙️voice_assistant.py
│   └── 5_💬Virtual_Doula.py
├── utils/
│   ├── ai_utils.py             # Groq AI wrapper
│   └── constants.py            # Pregnancy data
├── images/
│   └── MY BABY.png
├── .streamlit/
│   └── config.toml             # Theme configuration
├── requirements.txt
├── .env.example
└── README.md
```

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">Made with ❤️ for mothers everywhere</p>

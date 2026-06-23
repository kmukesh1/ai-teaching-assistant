import streamlit as st
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

try:
    from app.services.teaching_service import TeachingService
    teaching = TeachingService()
except:
    teaching = None

st.set_page_config(page_title="AI Teaching Assistant", page_icon="🎓", layout="wide")
st.title("🎓 AI Teaching Assistant - Your Personal Tutor")

st.sidebar.header("Settings")
provider = st.sidebar.selectbox("AI Model", ["gemini", "demo"])

mode = st.sidebar.radio("Teaching Mode", ["General Chat", "Explain Concept", "Quiz Generator", "Study Planner"])

query = st.chat_input("Ask anything about CS, AI, Math, Physics...")

if query:
    with st.chat_message("user"):
        st.write(query)
    with st.chat_message("assistant"):
        if teaching:
            if mode == "Explain Concept":
                response = teaching.explain_concept(query)
            else:
                response = teaching.llm.get_response(query)
        else:
            response = "Thanks for your question! Add your GEMINI_API_KEY in Secrets to get real AI answers."
        st.write(response)

st.info("Full features (RAG upload, Quiz generation, Assignments, Voice) are in the complete version. This is ready-to-use now!")
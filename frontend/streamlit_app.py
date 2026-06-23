import streamlit as st
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

st.set_page_config(page_title="AI Teaching Assistant", page_icon="🎓", layout="wide")
st.title("🎓 AI Teaching Assistant")
st.write("Your personal AI tutor is ready!")

st.info("This is a simplified version for quick deployment. The full version with all features is in the complete project.")

# Placeholder for full app
st.write("Upload your notes or ask any question about CS, AI, Math, Physics!")

query = st.text_input("Ask your question here:")
if query:
    st.success("Thank you! In the full version, the AI would answer here using Gemini or your chosen model.")

st.markdown("---")
st.caption("Full production version deployed from the complete codebase. Add your GEMINI_API_KEY in app secrets for real AI responses.")
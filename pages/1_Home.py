import streamlit as st

# Set up page configuration (optional)
st.set_page_config(
    page_title="College Explorer",
    page_icon="🎓",
    layout="wide"
)

# Main landing content
st.title("Welcome to the College Explorer")
st.write("""
Use the sidebar on the left to navigate between tools:
- 🔍 **Find Colleges** to search and shortlist schools
- 📊 **Manage Data** to review and edit college info
- 🗺️ **Map Universities** to analyze the best location for you
""")

#streamlit run streamlit_app.py

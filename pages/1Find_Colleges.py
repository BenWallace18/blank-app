import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Find Colleges",
    page_icon="🎓",
    layout="wide"
)
st.title("Find Your College")



# Load the college list
df = pd.read_csv("csv_files/names.csv")

# Initialize a shortlist in session state
if 'shortlist' not in st.session_state:
    st.session_state.shortlist = []

# Search bar
search_term = st.text_input("Search for a college:")

# Filter based on search term
if search_term:
    results = df[df['Name'].str.contains(search_term, case=False, na=False)]
else:
    results = df

for i, row in results.iterrows():
    col_name = row['Name']
    if col_name not in st.session_state.shortlist:
        if st.button(f"Add: {col_name}", key=f"add_{i}"):
            st.session_state.shortlist.append(col_name)
            st.rerun() 
    else:
        st.markdown(f"✅ **{col_name}** already added")




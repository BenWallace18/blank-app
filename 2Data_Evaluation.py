

import streamlit as st
import pandas as pd

def getColleges(list, df):
    if len(list) != 0:
        newlist = []
        for i in list:
            result = df[df['Name'] == i]
            newlist.append(result)
        return pd.concat(newlist, ignore_index=True)
    return None


# Access the public shortlist from session state
shortlist = st.session_state.get('shortlist', [])      


st.set_page_config(
    page_title="Data Evaluation",
    page_icon="🎓",
    layout="wide"
)
st.title("Evaluate Colleges")

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

if st.button("Clear List", type="primary"):
    shortlist.clear()



if not shortlist:
    st.write("No colleges have been added to the shortlist yet.")
else:
    st.subheader("📝 Your Current Shortlist")
    for college in shortlist:
        st.write("•", college)

st.subheader("How would you like to be contacted?")
option = st.selectbox(
    "",
    ("Average ACT", "Average SAT", "Graduation Rate", "Average Cost"),
)

match option: 
    case "Average ACT":
        df = getColleges(shortlist, pd.read_csv("csv_files/act_average.csv"))
    case "Average SAT":
        df = getColleges(shortlist, pd.read_csv("csv_files/sat_average.csv"))
    case "Graduation Rate":
        df = getColleges(shortlist, pd.read_csv("csv_files/graduation_rate.csv"))
    case "Average Cost":
        df = getColleges(shortlist, pd.read_csv("csv_files/cost_average.csv"))
    case _:
        df.write("")
        
st.write(df)


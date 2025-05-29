import streamlit as st
import pandas as pd
import pydeck as pdk

st.set_page_config(
    page_title="Map Viewer",
    page_icon="🎓",
    layout="wide"
)

st.title("View Map of Colleges")

def getColleges(list, df):
    if len(list) != 0:
        newlist = []
        for i in list:
            result = df[df['Name'] == i]
            newlist.append(result)
        return pd.concat(newlist, ignore_index=True)
    return None

shortlist = st.session_state.get('shortlist', [])    

df = getColleges(shortlist, pd.read_csv("csv_files/location.csv")) 

layer = pdk.Layer(
    "ScatterplotLayer",     
    data=df,                
    get_position='[lon, lat]',  
    get_radius = 5000,
    get_fill_color='[255, 0, 0, 160]',  
    pickable=True          
)


tooltip = {
    "html": "<b>{Name}</b>",   
    "style": {
        "backgroundColor": "gray",
        "color": "white"
    }
}

if len(shortlist) != 0:
    st.pydeck_chart(pdk.Deck(
        initial_view_state=pdk.ViewState(
            latitude=df['lat'].mean(),
            longitude=df['lon'].mean(),
            zoom=5
        ),
        layers=[layer],
        tooltip=tooltip
    ))
else:
    st.write("Add Colleges First")

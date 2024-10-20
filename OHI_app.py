import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#data loading
dt = pd.read_csv('/workspaces/gdp-dashboard-1/data/IOH.csv')
#dt.head()
#dt.fillna(0)
#print(dt)


st.title("Historical People Data Dashboard")

# Section 1: About the Project
st.header("About This Project")
st.markdown("""
This project aims to showcase historical individuals and their professional paths 
through interactive charts and tables. Users can explore various professions, 
view detailed resumes, and gain insights into the historical context of these individuals.
""")

# Section 2: Name selection and introduction
st.header("Select a Historical Figure")
selected_name = st.selectbox("Choose a name:", dt['IntervieweeName'])
if selected_name:
    person_info = dt[dt['IntervieweeName'] == selected_name].iloc[0]
    st.write(f"معرفی: {person_info['Intro']}")
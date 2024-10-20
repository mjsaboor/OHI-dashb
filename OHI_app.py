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
    st.write(f"معرفی: {person_info['Intro  ']}")

 # Section 3: Tabs for graphs/tables
st.header("Data Visualization")
tabs = st.tabs(["gender ratio", "country of education", "Profession Analysis"])

with tabs[0]:
    # Bar Chart for Experience Overview
    st.subheader("Experience Overview")
    country_counts = dt['University'].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=country_counts.index, y=country_counts.values, palette='viridis')
    plt.title("Number of Occurrences for Each Country")
    plt.xlabel("Country")
    plt.ylabel("Count")
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()  # Adjust layout to prevent clipping of tick-labels
    plt.show()

with tabs[1]:
    # Pie Chart for Field Distribution
    st.subheader("Field Distribution")


with tabs[2]:
    # Table of Professions
    st.subheader("Profession Analysis")
 
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#data loading
dt = pd.read_csv('/workspaces/gdp-dashboard-1/data/IOH-1.csv')

#App
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
tabs = st.tabs(["University Background", "Political Party", "Profession Analysis"])

with tabs[0]:
    # Bar Chart for Experience Overview
    st.subheader("University Background")
    country_counts = dt['University'].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=country_counts.index, y=country_counts.values, palette='viridis')
    plt.title("Number of Occurrences for Each Country")
    plt.xlabel("Country")
    plt.ylabel("Count")
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()  # Adjust layout to prevent clipping of tick-labels
    st.pyplot(plt)
    
with tabs[1]:
    # Pie Chart for Field Distribution
    st.subheader("Political Party")
    party_counts = dt['Party'].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=party_counts.index, y=party_counts.values, palette='flare')
    plt.title("Number of Occurrences for Each Party")
    plt.xlabel("Party")
    plt.ylabel("Count")
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()  # Adjust layout to prevent clipping of tick-labels
    st.pyplot(plt)


with tabs[2]:
    # Table of Professions
    st.subheader("Profession Analysis")
    
    ShahGov_count = dt['IsShahGov'].sum()
    ShahOpp_count = dt['IsShahOpp'].sum()

#   Data for pie chart
    labels = ['Pro-Shah', 'Anti-Shah']
    sizes = [ShahGov_count, ShahOpp_count]
    
    # Create a pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff'])
    plt.title("Ratio of the Pro-Shah & Anti-Shah interviewees")
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
    st.pyplot(plt)

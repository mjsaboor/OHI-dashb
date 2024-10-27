import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#data loading
dt = pd.read_csv('/workspaces/gdp-dashboard-1/data/IOH-2.csv')

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
    st.write(f"معرفی: {person_info['Intro']}")

 # Section 3: Tabs for graphs/tables
st.header("Data Visualization")
tabs = st.tabs(["Gender Ratio", "University Background", "Political Party", "Political Orientation", "Political career", "Position"])

with tabs[0]:
    # Table of Professions
    st.subheader("Gender Ratio")
    st.markdown("چند درصد مصاحبه شدگان زن یا مرد هستند؟")
    female_count = dt['female'].sum()
    male_count = len(dt['female']) - dt['female'].sum()

#   Data for pie chart
    labels = ['Female', 'Male']
    sizes = [female_count, male_count]
    
    # Create a pie chart
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#097969','#D70040'])
    plt.title("Gender ratio of interviewees")
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
    st.pyplot(plt)

with tabs[1]:
    # Bar Chart for Experience Overview
    st.subheader("University Background")
    st.markdown("مصاحبه شدگان در چه کشورهایی تحصیل کرده اند؟")
    country_counts = dt['University'].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=country_counts.index, y=country_counts.values, palette='viridis')
    plt.title("Number of Occurrences for Each Country")
    plt.xlabel("Country")
    plt.ylabel("Count")
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()  # Adjust layout to prevent clipping of tick-labels
    st.pyplot(plt)
    
with tabs[2]:
    # Pie Chart for Field Distribution
    st.subheader("Political Party")
    #dt['Party'].replace(0, np.nan, inplace=True)
    party_counts = dt['Party'].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=party_counts.index, y=party_counts.values, palette='flare')
    plt.title("Number of Occurrences for Each Party")
    plt.xlabel("Party")
    plt.ylabel("Count")
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()  # Adjust layout to prevent clipping of tick-labels
    st.pyplot(plt)


with tabs[3]:
    # Table of Professions
    st.subheader("Political Orientation")
    st.markdown("چه نسبتی از مصاحبه شدگان از طرفداران یا مخالفان شاه بوده اند؟")
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

with tabs[4]:
    # Table of Professions
    st.subheader("Political career")
    st.markdown("چه نسبتی از مصاحبه شدگان پیش و پس از انقلاب مسئولیت کاری داشته اند؟")
    PreRev_count = dt['PreRevolution'].sum()
    PosRev_count = dt['PostRevolution'].sum()

#   Data for pie chart
    labels = ['holding position before revolution', 'holding position after revolution']
    sizes = [PreRev_count, PosRev_count]
    
    # Create a pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#C1E1C1','#2E8B57'])
    plt.title("Ratio of interviewees holding position before/after revolution")
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
    st.pyplot(plt)

with tabs[5]:
    counts = dt[['Palement', 'Minister', 'Bussiness','ForeignAffairs','BankEco','Diplomat','Military','Press', 'Lawyer']].sum()
    new_labels = ['Parlement Member', 'Minister', 'Business', 'Foreign Affairs minister', 'Banking & Economy', 'Diplomat', 'Military', 'Press' ,'Lawyer']
# Plotting the results
    plt.figure(figsize=(8, 6))
    sns.barplot(x=new_labels, y=counts.values, palette="rocket")
    plt.xlabel("Category")
    plt.ylabel("Number of individuals")
    plt.ylim(0, dt.shape[0])  # Adjust y-limit based on total number of rows
    plt.title("Sum of Values by Category")
    plt.xticks(rotation='vertical')
    st.pyplot(plt)

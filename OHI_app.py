import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from bidi.algorithm import get_display
from arabic_reshaper import reshape

#data loading
dt = pd.read_csv('/workspaces/gdp-dashboard-1/data/IOH-3.csv')

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
    labels = ['0', 'فرانسه', 'ایران', 'آمریکا', 'آلمان']
    new_labels = [get_display(reshape(label)) for label in labels]
    plt.figure(figsize=(10, 6))
    sns.barplot(x=new_labels, y=country_counts.values, palette='viridis')
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
    labels = ['جبهه ملی', 'رستاخیز', 'نیروی سوم', 'حزب مردم', 'توده',
       'حزب پیکار', 'زحمتکشان', 'پان ایرانیسم', 'ایران نوین', 'مجاهدین خلق',
       'فدائیان خلق', 'نهضت آزادی', '0']
    new_labels = [get_display(reshape(label)) for label in labels]
    party_counts = dt['Party'].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=new_labels, y=party_counts.values, palette='flare')
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
    labels = ['موافقان شاه', 'مخالفان شاه']
    persian_labels = [get_display(reshape(label)) for label in labels]
    sizes = [ShahGov_count, ShahOpp_count]
    
    # Create a pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=persian_labels, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff'])
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
    labels = ['نماینده مجلس', 'وزیر', 'بازرگانان', 'وزیر امورخارجه', 'سازمان برنامه و بانک مرکزی', 'دیپلمات', 'نظامی', 'مطبوعات' ,'حقوقدان']
    new_labels = [get_display(reshape(label)) for label in labels]

# Plotting the results
    plt.figure(figsize=(8, 6))
    sns.barplot(x=new_labels, y=counts.values, palette="rocket")
    plt.xlabel("Category")
    plt.ylabel("Number of individuals")
    plt.ylim(0, dt.shape[0])  # Adjust y-limit based on total number of rows
    plt.title("Sum of Values by Category")
    plt.xticks(rotation='vertical')
    st.pyplot(plt)

#Section 4
st.header("Age Distribution")
tabs = st.tabs(["Age of interviewees", "Age & political status"])

with tabs[0]:
    st.subheader("وضعیت سن مصاحبه شدگان")
    specific_age = 60

    # Set up the histogram
    plt.figure(figsize=(10, 6))
    plt.hist(dt['Age'], bins=10, alpha=0.7, color='skyblue', edgecolor='black')
    
    # Add a vertical line for the specific age
    plt.axvline(x=specific_age, color='red', linestyle='dashed', linewidth=2)
    
    # Add text label for the specific age line
    plt.text(specific_age + 1, 5, f'Age = {specific_age}', color='red')
    
    # Title and labels
    plt.title(get_display(reshape("توزیع سن مصاحبه شدگان در زمان انجام مصاحبه")))
    plt.xlabel(get_display(reshape("سن")))
    plt.ylabel(get_display(reshape("تعداد مصاحبه شدگان")))
    plt.grid(axis='y', alpha=0.75)
    st.pyplot(plt)

with tabs[1]:
    dt['Group'] = dt.apply(lambda x: 'Pro-shah' if x['IsShahGov'] == 1 else 'Anti-shah', axis=1)

    # Set the style of the plot
    sns.set(style="whitegrid")

    # Create the box plot
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Group', y='Age', data=dt, palette={'Pro-shah': '#4361EE', 'Anti-shah': '#F72585'})

    # Add titles and labels
    plt.title('Age Distribution by Group')
    plt.xlabel('Group')
    plt.ylabel('Age')
    st.pyplot(plt)

    sns.set(style="whitegrid")

    # Create the scatter plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Age', y=dt.index, hue='Group', data=dt, palette={'Pro-shah': '#3A0CA3', 'Anti-shah': '#F72585'}, alpha=0.9)

    # Add titles and labels
    plt.title('Scatter Plot of Ages by Group')
    plt.xlabel('Age')
    plt.ylabel('Index')

    # Show the plot
    plt.legend(title='Group')
    st.pyplot(plt)
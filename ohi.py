import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/workspaces/gdp-dashboard-1/data/IOH.csv')

df.dtypes

c1 = df['IsShahGov'].sum()
c2 = df['IsShahOpp'].sum()

#   Data for pie chart
labels = ['had post under Shah', 'had post after Revolution']
sizes = ['c1', 'c2']
    
# Create a pie chart
sns.set(style="whitegrid")

# Create a pie chart
plt.figure(figsize=(8, 8))
# Use a Matplotlib pie chart but styled with Seaborn's aesthetics
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("pastel"))
plt.title("Ratio of A and B")
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
plt.show()
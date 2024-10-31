#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from bidi.algorithm import get_display
from arabic_reshaper import reshape

df = pd.read_csv('/workspaces/gdp-dashboard-1/data/IOH-2.csv')
#df1 = df.fillna(0)
#df.columns
L = df['University'].drop_duplicates()
print(L)
c1 = df['Palement'].sum()
c2 = df['Minister'].sum()
c3 = df['Bussiness'].sum()
counts = [c1, c2, c3]
#%%
plt.figure(figsize=(8, 6))
sns.barplot(x=counts.index, y=counts.values, palette="pastel")
#plt.xlabel("Columns")
#plt.ylabel("Count")
plt.ylim(0, df.shape[0])  # Adjust y-limit based on total number of rows
plt.show()


def make_farsi_text(x):
  reshaped_text = reshape(x)
  farsi_text = get_display(reshaped_text)
  return farsi_text

ShahGov_count = df['IsShahGov'].sum()
ShahOpp_count = df['IsShahOpp'].sum()

labels = ['موافقان شاه', 'مخالفان شاه']
persian_labels = [make_farsi_text(labels) for label in labels]
sizes = [ShahGov_count, ShahOpp_count]
    
    # Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=persian_labels, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff'])
plt.title("Ratio of the Pro-Shah & Anti-Shah interviewees")
plt.axis('equal')
#plt.ylim(0, dt.shape[0])  # Adjust y-limit based on total number of rows
plt.show()

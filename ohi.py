#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/workspaces/gdp-dashboard-1/data/IOH-2.csv')
#df1 = df.fillna(0)
#df.columns
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
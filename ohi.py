import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns

df = pd.read_csv('/workspaces/gdp-dashboard-1/data/IOH-1.csv')
#df1 = df.fillna(0)
#df1.to_csv('/workspaces/gdp-dashboard-1/data/IOH-1.csv')
df['IsShahGov'].sum()
print(df1)
df.dtypes
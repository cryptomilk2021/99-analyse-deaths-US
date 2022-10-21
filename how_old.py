import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# This might be helpful:
from collections import Counter
pd.options.display.float_format = '{:,.2f}'.format

# df_hh_income = pd.read_csv('Median_Household_Income_2015.csv', encoding="windows-1252")
# df_pct_poverty = pd.read_csv('Pct_People_Below_Poverty_Level.csv', encoding="windows-1252")
# df_pct_completed_hs = pd.read_csv('Pct_Over_25_Completed_High_School.csv', encoding="windows-1252")
# df_share_race_city = pd.read_csv('Share_of_Race_By_City.csv', encoding="windows-1252")
df_fatalities = pd.read_csv('Deaths_by_Police_US.csv', encoding="windows-1252")

df_age = df_fatalities['age']
df_age = df_age.dropna()
# print(df_age.columns)
df_age = df_age.to_frame()
df_age.to_csv('output.csv')
count = int((df_age['age'] > 25).sum())
total = int(len(df_age))
percentage = count / total * 100

print(f'% of ages > 25 : {round(percentage, 2)}%')

df = df_fatalities['age']
df = df.dropna()
df = df.to_frame()

k = len(df.columns)
n = 2
m = (k - 1) // n + 1
fig, axes = plt.subplots(m, n, figsize=(n * 5, m * 3))
for i, (name, col) in enumerate(df.iteritems()):
    r, c = i // n, i % n
    # ax = axes[r, c]
    ax = axes[r]
    col.hist(ax=ax)
    ax2 = col.plot.kde(ax=ax, secondary_y=True, title='age distribution')
    ax2.set_ylim(0)

fig.tight_layout()

plt.show()









exit()


df = df_fatalities
df = df.sort_values(by=['total'], ascending=True)
final_df = df['armed']

final_df = final_df.to_frame()
final_df['total'] = df['total'].copy()

final_df.to_csv('final.csv')
data = pd.read_csv('final.csv', encoding="windows-1252")

dataFrame = pd.DataFrame(data=data)

dataFrame.plot.bar(x="armed", y="total", rot=70, title="type of weapon", figsize=(20, 8))

plt.show(block=True)






plt.show()


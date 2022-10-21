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


# df_pct_poverty = df_pct_poverty.replace('-', 0)
#change Nan to U for unknown
df_fatalities['race'] = df_fatalities['race'].replace(np.nan, 'U')

df_fatalities = df_fatalities.groupby(['race'])['race'].count().reset_index(name='total')
df_fatalities.to_csv('output.csv')

colors = ['#FF0000', '#0000FF', '#FFFF00', '#ADFF2F', '#FFA500']

plt.pie(df_fatalities['total'], colors=colors, labels=df_fatalities['race'], autopct='%1.1f%%', pctdistance=0.85)  #, explode=explode)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()

fig.gca().add_artist(centre_circle)

plt.title('Deaths by Race')

plt.show()







exit()
df_pct_poverty['poverty_rate'] = pd.to_numeric(df_pct_poverty['poverty_rate'])

df_pct_poverty = df_pct_poverty.sort_values(by=['poverty_rate'], ascending=True)

df_pct_completed_hs = df_pct_completed_hs.replace('-', 0)
df_pct_completed_hs['percent_completed_hs'] = pd.to_numeric(df_pct_completed_hs['percent_completed_hs'])

df_pct_completed_hs = df_pct_completed_hs.groupby(['Geographic Area'])['percent_completed_hs'].mean()
df_pct_completed_hs = df_pct_completed_hs.to_frame()
df_pct_completed_hs = df_pct_completed_hs.sort_values(by=['percent_completed_hs'], ascending=True)

# df_pct_completed_hs.plot(kind="line", title='% completed high school, by State (US)', figsize=(11, 6))

df_pct_completed_hs.to_csv('_hs.csv')

df_pct_completed_hs.sort_values(by=['Geographic Area'], inplace=True)
df_pct_poverty.sort_values(by=['Geographic Area'], inplace=True)
# print(df_pct_completed_hs)
# print(df_pct_poverty)
df_combined = df_pct_poverty.copy()
df_combined['percent_completed_hs'] = df_pct_completed_hs['percent_completed_hs'].copy()
df_combined.sort_values(by=['poverty_rate'], inplace=True)

sns.jointplot(x = 'percent_completed_hs',y = 'poverty_rate',data = df_combined,kind = 'kde')
plt.show()
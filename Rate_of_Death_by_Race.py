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

df_fatalities.race = df_fatalities.race.fillna('O')
df = df_fatalities.groupby(['city'])['city'].count().reset_index(name='total')

df = df.sort_values(by=['total'], ascending=False)
#get list of top cities
race_list = []
race_list = df_fatalities.race.unique()

city_list = []
for i, row in df.iloc[:10].iterrows():
    # print(f"city: {row['city']} - number of deaths: {row['total']}")
    city_list.append(row['city'])

#get data for those cities
df_bare = df_fatalities[df_fatalities['city'].isin(city_list)]
df1 = df_bare.groupby(['city','race']).count()
df1.to_csv('temp.csv')
df2 = df1.filter(['city','race','id'], axis=1)


df2.plot(kind="bar", figsize=(15,8))
plt.show()

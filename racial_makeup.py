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
df_share_race_city = pd.read_csv('Share_of_Race_By_City.csv', encoding="windows-1252")
# df_share_race_city = pd.read_csv('Share_of_Race_By_City_small.csv', encoding="windows-1252")
# df_fatalities = pd.read_csv('Deaths_by_Police_US.csv', encoding="windows-1252")

column_names = list(df_share_race_city)
df_share_race_city = df_share_race_city.replace('(X)', 0)

#change columns to float
for i in range(2, len(column_names)):
    df_share_race_city[column_names[i]] = df_share_race_city[column_names[i]].astype(float)

df_share_race_city_base = df_share_race_city.groupby(['Geographic area'])['share_white'].mean()

df_share_race_city_base = df_share_race_city_base.to_frame()

for i in range(3, len(column_names)):
    df_temp = df_share_race_city.groupby(['Geographic area'])[column_names[i]].mean()
    df_temp = df_temp.to_frame()
    df_share_race_city_base[column_names[i]] = df_temp[column_names[i]].copy()

df_share_race_city_base.to_csv('test.csv')

df_share_race_city_base.plot(kind="bar", title='racial makeup', figsize=(11, 6))

plt.show()
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
df_pct_completed_hs = pd.read_csv('Pct_Over_25_Completed_High_School.csv', encoding="windows-1252")
# df_share_race_city = pd.read_csv('Share_of_Race_By_City.csv', encoding="windows-1252")
# df_fatalities = pd.read_csv('Deaths_by_Police_US.csv', encoding="windows-1252")

df_pct_completed_hs = df_pct_completed_hs.replace('-', 0)
df_pct_completed_hs['percent_completed_hs'] = pd.to_numeric(df_pct_completed_hs['percent_completed_hs'])

df = df_pct_completed_hs.groupby(['Geographic Area'])['percent_completed_hs'].mean()
df = df.to_frame()
df = df.sort_values(by=['percent_completed_hs'], ascending=True)
print(f'lowest = {df.iloc[0]}')
print(f'highest = {df.iloc[-1]}')

print(df)
print(df.dtypes)
df.plot(kind="bar", title='% completed high school, by State (US)', figsize=(11, 6))

plt.show()

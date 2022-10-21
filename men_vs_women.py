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

df_fatalities = df_fatalities.groupby(['gender'])['gender'].count().reset_index(name='total')
df_fatalities.to_csv('output.csv')
df_fatalities.plot(kind="bar", figsize=(11, 6))

plt.title('Men vs Women')

plt.show()


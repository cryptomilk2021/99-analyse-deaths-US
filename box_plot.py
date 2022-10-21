import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

pd.options.display.float_format = '{:,.2f}'.format

# df_hh_income = pd.read_csv('Median_Household_Income_2015.csv', encoding="windows-1252")
# df_pct_poverty = pd.read_csv('Pct_People_Below_Poverty_Level.csv', encoding="windows-1252")
# df_pct_completed_hs = pd.read_csv('Pct_Over_25_Completed_High_School.csv', encoding="windows-1252")
# df_share_race_city = pd.read_csv('Share_of_Race_By_City.csv', encoding="windows-1252")
df_fatalities = pd.read_csv('Deaths_by_Police_US.csv', encoding="windows-1252")

df_box_plot = df_fatalities['gender'].copy()
df_box_plot = df_box_plot.to_frame()

df_box_plot['age'] = df_fatalities['age'].copy()
df_box_plot['manner_of_death'] = df_fatalities['manner_of_death'].copy()

#delete NaN 'age' rows
df_box_plot = df_box_plot[df_box_plot['age'].notna()]
df_box_plot.to_csv('test.csv')


sns.catplot(data=df_box_plot, kind='box', col='gender', x='manner_of_death', y='age', hue='manner_of_death', sharey=False, height=4)
plt.show()




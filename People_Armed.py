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

df_fatalities1 = df_fatalities.groupby(['gender'])['gender'].count().reset_index(name='total')

male = int(df_fatalities1[df_fatalities1.gender == 'M'].total)
female = int(df_fatalities1[df_fatalities1.gender == 'F'].total)
total = male + female
male = "{:.2f}".format(male / total * 100)
female = "{:.2f}".format(female / total * 100)

print(f'female = {female}%\nmale = {male}%')

unarmed = len(df_fatalities[df_fatalities['armed'] == 'unarmed'])
guns_used = len(df_fatalities[df_fatalities['armed'] == 'gun'])

print(f'unarmed = {unarmed}\nguns = {guns_used}')

df_fatalities = df_fatalities.groupby(['armed'])['armed'].count().reset_index(name='total')
df_fatalities.to_csv('output.csv')


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


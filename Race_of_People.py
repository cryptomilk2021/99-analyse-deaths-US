import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy


df_fatalities = pd.read_csv('Deaths_by_Police_US.csv', encoding="windows-1252")
df_fatalities.race = df_fatalities.race.fillna('O')
df_fatalities = df_fatalities[df_fatalities['age'].notna()]
#
list_of_races = df_fatalities['race'].unique()
df_races = pd.DataFrame()

df_temp = pd.DataFrame()
df_temp1 = pd.DataFrame()
df_temp2 = pd.DataFrame()

for i in list_of_races:
    df_temp = df_fatalities.loc[df_fatalities['race'] == i]
    df_temp = df_temp['age']
    df_temp1[i] = df_temp
    df_temp2 = pd.concat([df_temp2, df_temp1], ignore_index=False, axis=1)
    df_temp = pd.DataFrame()
    df_temp1 = pd.DataFrame()

list_count = []

for i in list_of_races:
    list_count.append(df_temp2[i].count())

plt.bar(list_of_races,list_count, label="deaths by race")
plt.legend()

# The following commands add labels to our figure.
plt.xlabel('Race')
plt.ylabel('nbr of deaths')
plt.title('deaths by race')

plt.show()

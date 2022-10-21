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


k = len(df_temp2.columns)
n = 2
m = (k - 1) // n + 1
fig, axes = plt.subplots(m, n, figsize=(n * 5, m * 3))
for i, (name, col) in enumerate(df_temp2.iteritems()):
    r, c = i // n, i % n
    ax = axes[r, c]
    col.hist(ax=ax)
    ax2 = col.plot.kde(ax=ax, secondary_y=True, title=name)
    ax2.set_ylim(0)

fig.tight_layout()

plt.show()

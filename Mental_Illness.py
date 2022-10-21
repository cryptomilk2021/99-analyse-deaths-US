import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy

df_fatalities = pd.read_csv('Deaths_by_Police_US.csv', encoding="windows-1252")
df_fatalities.race = df_fatalities.race.fillna('O')
df_fatalities = df_fatalities[df_fatalities['signs_of_mental_illness'].notna()]
#
list_of_ans = df_fatalities['signs_of_mental_illness'].unique()

nbr_of_deaths = int(df_fatalities['signs_of_mental_illness'].count())
nbr_mental_ill = int((df_fatalities['signs_of_mental_illness'] == True).sum())


print(f'mental illness in killings = {round(nbr_mental_ill / nbr_of_deaths * 100, 2)} %')
exit()

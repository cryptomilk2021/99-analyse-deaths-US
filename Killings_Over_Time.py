import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy


df_fatalities = pd.read_csv('Deaths_by_Police_US.csv', encoding="windows-1252")


df_fatalities['date'] = pd.to_datetime(df_fatalities['date'])
#group by state, count
min_date = df_fatalities['date'].min()
max_date = df_fatalities['date'].max()
list_dates = []
list_killings = []
print(min_date)
print(max_date)

df = df_fatalities.groupby(['date'])['date'].count().reset_index(name='deaths')
list_dates = df['date'].to_list()
list_killings = df['deaths'].to_list()
# print(df)

# print (df.groupby([df['date'].dt.year.rename('year'),df['date'].dt.month_name().rename('month')])['deaths'].sum().reset_index())
df = df.groupby([df['date'].dt.year.rename('year'),df['date'].dt.month_name().rename('month')])['deaths'].sum().reset_index()
print(df)
# exit()
df1 = pd.DataFrame()
df1["Period"] = df['year'].astype(str) +" "+ df["month"]
df1['deaths'] = df['deaths'].copy()
list_dates = df1['Period'].to_list()
list_killings = df1['deaths'].to_list()

plt.bar(list_dates,list_killings)
plt.legend()

# The following commands add labels to our figure.
plt.xlabel('Time')
plt.ylabel('nbr of deaths')
plt.title('deaths over time')

plt.show()

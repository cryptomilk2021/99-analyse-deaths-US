import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
# from plotly import express
# import plotly_express
import plotly.express as px

df_fatalities = pd.read_csv('Deaths_by_Police_US.csv', encoding="windows-1252")

#group by state, count
df = df_fatalities.groupby(['state'])['state'].count().reset_index(name='total deaths')

fig = px.choropleth(df,
                    locations='state',
                    locationmode="USA-states",
                    scope="usa",
                    color='total deaths',
                    color_continuous_scale="Viridis_r",

                    )
fig.show()
exit()

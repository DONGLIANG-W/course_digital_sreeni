import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import plotly.express as px
from plotly.offline import plot
# load the data
covid_confirmed = pd.read_csv('../data/time_series_covid19_confirmed_global.csv')
covid_death = pd.read_csv('../data/time_series_covid19_deaths_global.csv')
covid_recovered = pd.read_csv('../data/time_series_covid19_recovered_global.csv')
# preprocess the data, rename country name, focus on China datasets
covid_confirmed['Country/Region'].replace('Mainland China', 'China', inplace=True)
covid_death['Country/Region'].replace('Mainland China', 'China', inplace=True)
covid_recovered['Country/Region'].replace('Mainland China', 'China', inplace=True)
# fill the na
covid_confirmed[['Province/State']] = covid_confirmed[['Province/State']].fillna('')
covid_confirmed.fillna(0, inplace=True)
covid_death[['Province/State']] = covid_death[['Province/State']].fillna('')
covid_death.fillna(0, inplace=True)
covid_recovered[['Province/State']] = covid_recovered[['Province/State']].fillna('')
covid_recovered.fillna(0, inplace=True)
# start by aggregating all the cases t see a snapshot for the world
covid_confirmed_count = covid_confirmed.iloc[:, 4:].sum().max()
covid_death_count = covid_death.iloc[:, 4:].sum().max()
covid_recovered_count = covid_recovered.iloc[:, 4:].sum().max()
print('Total confirmed {}, death {}, recovered {}'.format(covid_confirmed_count,
                                                         covid_death_count,
                                                         covid_recovered_count))
# to plot the case, store the numbers in a dataframe

world_df = pd.DataFrame({
    'Confirmed': [covid_recovered_count],
    'Death': [covid_recovered_count],
    'Recovered': [covid_recovered_count],
    'Active': [covid_confirmed_count-covid_recovered_count-covid_death_count]
})
print(world_df)
world_long_df = world_df.melt(value_vars=['Active', 'Death', 'Recovered'],
                              var_name='status',
                              value_name='count')
world_long_df['upper'] = 'confirmed'
print(world_long_df)

fig = px.treemap(world_long_df, path=['status'], values='count',
                 color_discrete_sequence=['#3498db', '#2ecc71', '#e74c3c'],
                 template='plotly_dark')
plot(fig)
# plot using the matplot.pyplot module
covid_world_confirmed = covid_confirmed.iloc[:, 4:].sum(axis=0)
covid_world_death = covid_death.iloc[:, 4:].sum(axis=0)
covid_world_recovered = covid_recovered.iloc[:, 4:].sum(axis=0)
covid_world_active = covid_world_confirmed-covid_world_recovered-covid_world_death
fig, ax = plt.subplots(figsize=(16, 6))
sns.lineplot(x=covid_world_active.index, y=covid_world_active, sort=False)
sns.lineplot(x=covid_world_confirmed.index, y=covid_world_confirmed, sort=False)
sns.lineplot(x=covid_world_death.index, y=covid_world_death, sort=False)
sns.lineplot(x=covid_world_recovered.index, y=covid_world_recovered, sort=False)
ax.lines[0].set_linestyle('--')
plt.suptitle('Evolution of COVID-19 worldwide cases',
             fontsize=16,
             fontweight='bold')
plt.xticks(rotation=90)
plt.ylabel('Number of cases')
plt.legend(['Active', 'Confirmed', 'Death', 'Recovered'])
plt.show()
# plotting the data onto a map
covid_confirmed_agg = covid_confirmed.groupby('Country/Region').sum().reset_index()
covid_confirmed_agg.loc[:, ['Lat', 'Long']] = \
    covid_confirmed.groupby('Country/Region').mean().reset_index().loc[:, ['Lat', 'Long']]
MIN_CASES = 1000
covid_confirmed_agg = covid_confirmed_agg[covid_confirmed_agg.iloc[:, 3:].max(axis=1) > MIN_CASES]
print(covid_confirmed_agg.shape)
#Unpivot the DataFrame from wide to long format
covid_confirmed_agg_long = pd.melt(covid_confirmed_agg,
                                   id_vars=covid_confirmed_agg.iloc[:, :3],
                                   var_name='date',
                                   value_vars=covid_confirmed_agg.iloc[:, 3:],
                                   value_name='date_confirmed_cases')
#print(covid_confirmed_agg_long.shape)

#Plotly for visualization.
fig = px.scatter_geo(covid_confirmed_agg_long,
                     lat="Lat", lon="Long", color="Country/Region",
                     hover_name="Country/Region", size="date_confirmed_cases",
                     size_max=50, animation_frame="date",
                     template='plotly_dark', projection="natural earth",
                     title="COVID-19 worldwide confirmed cases over time")

plot(fig)






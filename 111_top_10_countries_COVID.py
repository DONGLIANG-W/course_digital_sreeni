import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":
    # read the csv file
    df_confirmed = pd.read_csv('data/time_series_covid19_confirmed_global.csv')
    df_death = pd.read_csv('data/time_series_covid19_deaths_global.csv')
    df_recovered = pd.read_csv('data/time_series_covid19_recovered_global.csv')
    # print the shape
    print("The shape of the data for confirmed cases is {}, deaths is {} and recovered is {}"
          .format(df_confirmed.shape, df_death.shape, df_recovered.shape))
    # converting all data into the long format
    df_confirmed_long = pd.melt(df_confirmed,
                                id_vars=df_confirmed.iloc[:, :4],
                                var_name='date',
                                value_name='confirmed')
    df_death_long = pd.melt(df_death,
                            id_vars=df_death.iloc[:, :4],
                            var_name='date',
                            value_name='death')
    df_recovered_long = pd.melt(df_death,
                                id_vars=df_recovered.iloc[:, :4],
                                var_name='date',
                                value_name='recovered')
    df_combined = df_confirmed_long
    df_combined['death'] = df_death_long['death']
    df_combined['recovered'] = df_recovered_long['recovered']
    df_combined['active'] = df_combined.confirmed-df_combined.recovered-df_combined.death
    df_combined['Country/Region'].replace('Mainland China', 'China', inplace=True)
    df_combined[['Province/State']] = df_combined[['Province/State']].fillna('')
    df_combined.fillna(0, inplace=True)
    df_country = df_combined.groupby(['Country/Region', 'Province/State']).max().reset_index()
    df_country = df_country.groupby('Country/Region').sum().reset_index()
    df_country.drop(['Lat', 'Long'], axis=1, inplace=True)
    top_10_country_confirmed = df_country.sort_values(by='confirmed', ascending=False).head(10)
    plt.bar(top_10_country_confirmed['Country/Region'], top_10_country_confirmed['confirmed'])
    plt.xticks(rotation=25)
    plt.title('Top 10 countries of confirmed cases')
    plt.xlabel('Country')
    plt.ylabel('Cases')
    plt.show()
    top_10_country_death = df_country.sort_values(by='death', ascending=False).head(10)
    plt.bar(top_10_country_death['Country/Region'], top_10_country_death['death'])
    plt.xticks(rotation=25)
    plt.title('Top 10 countries of death cases')
    plt.xlabel('Country')
    plt.ylabel('Cases')
    plt.show()
    top_10_country_recovered = df_country.sort_values(by='recovered', ascending=False).head(10)
    plt.bar(top_10_country_recovered['Country/Region'], top_10_country_recovered['death'])
    plt.xticks(rotation=25)
    plt.title('Top 10 countries of recovered cases')
    plt.xlabel('Country')
    plt.ylabel('Cases')
    plt.show()




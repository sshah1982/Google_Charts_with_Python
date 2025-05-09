import pandas as pd
from app.config.AppUrls import AppUrls
from app.util.ChartConstants import _ChartConstants
from os.path import sep

appUrls = AppUrls()

# Read clean CSV
df_imdb = pd.read_csv(appUrls._cleaned_csv_url, sep = ",", header = 0, skipinitialspace = True)

# Create a new_income field by separating $ sign for further calculations
df_imdb.loc[:, 'Income'] = df_imdb['Income'].apply(lambda x: str(x).split('$')[1])

# Create a new dataframe containing Country and Income
df_imdb_chart = df_imdb[['Country', 'Income']]

# As Income is number, replace all O and o with 0, replace all commas with space 
df_imdb_chart.loc[:, 'Income'] = df_imdb_chart.Income.map(lambda x: str(x).replace('O', '0'))
df_imdb_chart.loc[:, 'Income'] = df_imdb_chart.Income.map(lambda x: str(x).replace('o', '0'))
df_imdb_chart.loc[:, 'Income'] = df_imdb_chart.Income.map(lambda x: str(x).replace(',', ''))

# Convert Income to float 
df_imdb_chart.loc[:, 'Income'] = df_imdb_chart['Income'].astype('float64')

# Drop all temporary income fields and create new data frame containing only 
# Country and Income for further calculations
df_imdb_chart_final = df_imdb_chart[['Country', 'Income']]

# Apply group by Country and find average of incomes per country
df_imdb_chart_final = df_imdb_chart_final.reset_index().groupby('Country', as_index = False)['Income'].mean()

# Rename Income to Avg_Income
df_imdb_chart_final.rename(columns={"Income": "Avg_Income"})

# Write Bar Chart CSV to designated location
df_imdb_chart_final.to_csv(appUrls._charts_folder_path + sep + _ChartConstants.BAR + ".csv", index = False)


import pandas as pd
from app.config.AppSettings import AppSettings
from app.config.AppUrls import AppUrls
import csv

def replace_country_names(my_str):
    
    if my_str == 'Italy1':
        my_str = my_str.replace('Italy1', 'Italy')
    elif my_str == 'New Zeland':
        my_str = my_str.replace('New Zeland', 'New Zealand')
    elif my_str == 'New Zesland':
        my_str = my_str.replace('New Zesland', 'New Zealand')
    elif my_str == 'US.':
        my_str = my_str.replace('US.', 'USA')
    elif my_str == 'US':
        my_str = my_str.replace('US', 'USA')
    elif my_str == 'West Germany': 
        my_str = my_str.replace('West Germany', 'Germany')
    
    return my_str

appUrls = AppUrls()
settings = AppSettings()

# Reads raw file from designated location
df_imdb = pd.read_csv(appUrls._raw_csv_url, sep=";", header=0, skipinitialspace=True, encoding="Windows-1252")

# Drop completely blank rows
df_imdb.dropna(axis=0, how="all", inplace=True)

# Drop completely blank columns
df_imdb.dropna(axis=1, how="all", inplace=True)

df_imdb.loc[:, 'Country'] = df_imdb.Country.map(lambda x: replace_country_names(x))

# Write cleaned file to designated location
df_imdb.to_csv(appUrls._cleaned_csv_url, index = False, quoting=csv.QUOTE_ALL)
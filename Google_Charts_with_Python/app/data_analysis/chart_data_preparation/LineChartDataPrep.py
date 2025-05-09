import pandas as pd
from app.config.AppUrls import AppUrls
import dateutil.parser as dparser
from app.util.ChartConstants import _ChartConstants
from os.path import sep

appUrls = AppUrls()

# Read clean CSV
df_imdb = pd.read_csv(appUrls._cleaned_csv_url, sep = ",", header = 0, skipinitialspace = True)

df_imdb_chart = df_imdb[['Release year']]

dt_lst = df_imdb_chart['Release year'].to_list()

year_lst = []

for i in range(len(dt_lst)):
    try:
        dt_obj = dparser.parse(dt_lst[i], fuzzy=True)
        year_lst.append(dt_obj.year)
    except:
        try:
            tokens = dt_lst[i].split("-")
            year_lst.append(tokens[0])
        except:
            tokens = dt_lst[i].split(" ")
            year_lst.append(tokens[len(tokens) - 1])
 
df_years = pd.DataFrame({'Year': year_lst})

# Apply group by Year and find counts
df_imdb_chart_final = df_years.reset_index().groupby('Year', as_index = False).count()

# Write Line Chart CSV to designated location
df_imdb_chart_final.to_csv(appUrls._charts_folder_path + sep + _ChartConstants.LINE + ".csv", index = False)
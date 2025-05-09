import pandas as pd
from app.config.AppUrls import AppUrls
from app.util.ChartConstants import _ChartConstants
from os.path import sep

appUrls = AppUrls()

# Read clean CSV
df_imdb = pd.read_csv(appUrls._cleaned_csv_url, sep = ",", header = 0, skipinitialspace = True)

df_imdb_chart = df_imdb[['Content Rating']]

# Apply group by Content Rating and find counts
df_imdb_chart_final = df_imdb_chart.reset_index().groupby('Content Rating', as_index = False).count()

# Write Area Chart CSV to designated location
df_imdb_chart_final.to_csv(appUrls._charts_folder_path + sep + _ChartConstants.AREA + ".csv", index = False)
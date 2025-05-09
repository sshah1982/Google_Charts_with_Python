import pandas as pd
import numpy as np
import re
from app.config.AppUrls import AppUrls
from app.util.ChartConstants import _ChartConstants
from os.path import sep

def replace_more_than_one_decimals(my_str):
    dec_cnt = count_dots(my_str)
    
    if dec_cnt == 0:
        pass
    elif dec_cnt == 1:
        pass
    else:
        my_str = my_str.replace('.', '', 1)
    
    return my_str
        
def count_dots(my_str):
    regex = re.compile(r'\.')
    
    dec_cnt = len(regex.findall(my_str))
    
    return dec_cnt

def replace_numbers_greater_than_10(my_str):
    
    my_float = float(my_str)
    
    new_float = my_float
    
    if my_float > 10.0:
        new_float = my_float / 10.0
    
    return new_float

appUrls = AppUrls()

# Read clean CSV
df_imdb = pd.read_csv(appUrls._cleaned_csv_url, sep = ",", header = 0, skipinitialspace = True)

# Create a new dataframe containing Score column only
df_imdb_chart = df_imdb[['Score']]

# As Score is number, replace all :, -, , with . and f, e, +, ++ with space.
df_imdb_chart.loc[:, 'Score'] = df_imdb_chart.Score.map(lambda x: str(x).replace('e-0', ''))
df_imdb_chart.loc[:, 'Score'] = df_imdb_chart.Score.map(lambda x: str(x).replace('-', ''))
df_imdb_chart.loc[:, 'Score'] = df_imdb_chart.Score.map(lambda x: str(x).replace('f', ''))
df_imdb_chart.loc[:, 'Score'] = df_imdb_chart.Score.map(lambda x: str(x).replace('e', ''))
df_imdb_chart.loc[:, 'Score'] = df_imdb_chart.Score.map(lambda x: str(x).replace('+', ''))
df_imdb_chart.loc[:, 'Score'] = df_imdb_chart.Score.map(lambda x: str(x).replace('++', ''))
df_imdb_chart.loc[:, 'Score'] = df_imdb_chart.Score.map(lambda x: str(x).replace(':', '.'))
df_imdb_chart.loc[:, 'Score'] = df_imdb_chart.Score.map(lambda x: str(x).replace(',', '.'))
df_imdb_chart.loc[:, 'Score'] = df_imdb_chart.Score.map(lambda x: replace_more_than_one_decimals(x))
df_imdb_chart.loc[:, 'Score'] = df_imdb_chart.Score.map(lambda x: replace_numbers_greater_than_10(x))

# Convert scores to float 
df_imdb_chart.loc[:, 'Score'] = df_imdb_chart['Score'].astype('float64')

# Convert to numpy array
scores = df_imdb_chart.to_numpy()

# Define bin edges
bins = [7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0]  

# Get bin counts and edges
counts, bin_edges = np.histogram(scores, bins = bins)

csv_array = []
csv_array.append("Bins, Counts")

csv_text = ""
for i in range(0, len(bin_edges) - 1):
    csv_text = "[" + str(bin_edges[i]) + " - " +  str(bin_edges[i+1]) + "]" + ", " + str(counts[i])
    csv_array.append(csv_text)

pie_chart_csv_final_url = appUrls._charts_folder_path + sep + _ChartConstants.PIE + ".csv"
with open(pie_chart_csv_final_url, "w") as output:
    for i in range(0, len(csv_array)):
        output.write(csv_array[i])
        output.write("\n")



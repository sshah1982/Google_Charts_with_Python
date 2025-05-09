import pandas as pd
from app.config.AppUrls import AppUrls
from app.models.CsvData import CsvData
from os.path import sep

appUrls = AppUrls()

class CsvDataReader:
    _chart_data = None
    
    def __init__(self, chart_type):
        
        df_imdb = None
        
        chart_csv_path = appUrls._charts_folder_path + sep + chart_type + '.csv'
        df_imdb = pd.read_csv(chart_csv_path, sep = ",", header=0, skipinitialspace=True)
        
        column_names = list(df_imdb)
        
        data = df_imdb.values.tolist()
    
        self._chart_data = CsvData(column_names, data)
         


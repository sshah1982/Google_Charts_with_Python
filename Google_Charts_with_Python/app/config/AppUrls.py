import os
from os.path import sep
from app.config.AppSettings import AppSettings

appSettings = AppSettings()

class AppUrls:
    
    _raw_csv_url = ""
    _cleaned_csv_url = ""
    _charts_folder_path = ""
    
    def __init__(self):
         
        #Raw CSV
        url_list = [os.getcwd(), appSettings._app_root, appSettings._data_files_folder]
        url_list.append(appSettings._raw_csv_path)
        
        self._raw_csv_url = sep.join(url_list)
        
        #Clean CSV
        url_list = [os.getcwd(), appSettings._app_root, appSettings._data_files_folder]
        url_list.append(appSettings._cleaned_csv_path)

        self._cleaned_csv_url = sep.join(url_list)
        
        #Chart CSVs
        url_list = [os.getcwd(), appSettings._app_root, appSettings._charts_folder_path]
        self._charts_folder_path = sep.join(url_list)
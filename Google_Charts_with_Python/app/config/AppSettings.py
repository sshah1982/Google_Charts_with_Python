import configparser
import os
from pathlib import Path

path = Path(__file__)
root_dir = path.parent.absolute()

config = configparser.ConfigParser()
config_path = os.path.join(root_dir, "config.properties")

config.read(config_path)

class AppSettings:
    _scheme= ""
    _raw_data_url = ""
    _branch_name = ""
    _common_account = ""
    _repo_name = ""
    _token = ""
    _app_root = ""
    _data_files_folder = ""
    _raw_csv_path = ""
    _cleaned_csv_path = ""
    _charts_folder_path = ""
    
    def __init__(self):
        props = config["SCHEME"]
        self._scheme = "/".join(str(val) for key, val in props.items())
        
        props = config["RAW_DATA_URL"]
        self._raw_data_url = "/".join(str(val) for key, val in props.items())
        
        props = config["BRANCH_NAME"]
        self._branch_name = "/".join(str(val) for key, val in props.items())
        
        props = config["COMMON_ACCOUNT_NAME"]
        self._common_account = "/".join(str(val) for key, val in props.items())
        
        props = config["COMMON_REPO_NAME"]
        self._repo_name = "/".join(str(val) for key, val in props.items())
        
        props = config["TOKEN"]
        self._token = "/".join(str(val) for key, val in props.items())
        
        props = config["APP_ROOT"]
        self._app_root = "/".join(str(val) for key, val in props.items())
        
        props = config["DATA_FILES_FOLDER"]
        self._data_files_folder = "/".join(str(val) for key, val in props.items())
        
        props = config["RAW_CSV"]
        self._raw_csv_path = "/".join(str(val) for key, val in props.items())
        
        props = config["CLEANED_CSV"]
        self._cleaned_csv_path = "/".join(str(val) for key, val in props.items())
        
        props = config["CHARTS_FOLDER_PATH"]
        self._charts_folder_path = "/".join(str(val) for key, val in props.items())
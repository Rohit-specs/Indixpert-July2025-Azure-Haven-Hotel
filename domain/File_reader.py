import os 
import json
from domain import log

def file_reader(file_path,module_name):
    # if not os.path.exists(file_path):
    #     print("The file not exists in given path")
    #     return []
    with open(file_path,'r') as file:
        try:
            data=file.read()
        except Exception as error:
            log_obj=log(error,module_name)
            print("Error occurring while loading given json file path")
        
        try:
            data=json.loads(data)
        except Exception as error:
            log_obj=log(error,module_name)
            print("Please check if this path file is a valid json")
        return data

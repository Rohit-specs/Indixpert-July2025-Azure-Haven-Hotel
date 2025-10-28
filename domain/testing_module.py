import os 
import json

def file_reader(file_path,module_name):
    if not os.path.exists(file_path):
        print("The file not exists in given path")
        return
    with open(file_path,'r') as file:
        data=file.read()
        data=json.loads(data)
        return data

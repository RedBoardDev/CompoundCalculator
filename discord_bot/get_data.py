import os
import json
import orjson
from datetime import datetime

def f_set_height(height:int) -> None:
    with open('data.json', 'r') as file:
        data = orjson.loads(file.read())
    data['last_height'] = height
    with open('data.json', 'w') as file:
        json.dump(data, file, indent = 4)

def f_get_height() -> int:
    with open("data.json", "r") as file:
        data = orjson.loads(file.read())
    return(data['last_height'])

def get_localtime():
    current_time = datetime.now()
    return (current_time)

def set_var_dotenv(var_name:str):
    return (os.getenv(var_name))

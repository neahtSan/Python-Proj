import requests
import json
import base64
import os
import pathlib

gateway = ""
payload={}
headers = {'Content-Type': 'application/json'}

def view():
    path = "/Activity-5-Lambda" 
    url = f'{gateway}{path}'
    return print(requests.request("GET", url, headers=headers, data=payload).json())

def get(fileName):
    path = "/Activity-5-download" 
    url = f'{gateway}{path}'
    payload = json.dumps({
    "file": "mika.jpg"
    })
    
    file = requests.request("GET", url, headers=headers, data=payload)
    text = file.text
    base64_message = bytes(text, "utf-8")
    
    directory = pathlib.Path(__file__).parent.resolve()
    string_directory = str(directory)
    list_directory = string_directory.split('\\')
    save_directory = '\\'.join(list_directory[0:-1]+['download'])
    
    name = 'test1.txt'
    file_path = os.path.join(save_directory, name)
    if not os.path.isdir(directory):
        os.mkdir(directory)
    
    with open(file_path, "wb") as fh:
        fh.write(base64.decodebytes(base64_message))
    
    return print(save_directory, type(directory))


#url = 'http://google.com/favicon.ico'
#r = requests.get(url, allow_redirects=True)
#open('google.ico', 'wb').write(r.content)
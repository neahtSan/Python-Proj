import requests
import json
import base64
import os
from myPath import *

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
    
    save_directory = download_path()
    
    name = 'test1.txt'
    file_path = os.path.join(save_directory, name)
    
    with open(file_path, "wb") as fh:
        fh.write(base64.decodebytes(base64_message))
    
    return print(save_directory)


#url = 'http://google.com/favicon.ico'
#r = requests.get(url, allow_redirects=True)
#open('google.ico', 'wb').write(r.content)
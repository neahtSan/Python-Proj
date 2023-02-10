import requests
import json
import base64
import os
from components.myPath import *
from components.check import *

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
    "fileName": f'{fileName}'
    })
    
    file = requests.request("POST", url, headers=headers, data=payload)
    
    if file.status_code != 200:
        return print(file.text)
    
    rawText = file.text
    base64_message = bytes(rawText, "utf-8")
    
    save_directory = download_path()
    
    file_path = os.path.join(save_directory, fileName)
    
    with open(file_path, "wb") as fh:
        fh.write(base64.decodebytes(base64_message))
    
    return print(f'download {fileName} at {save_directory} complete!')

def put(fileName):
    path = "/Activity-5-upload"
    url = f'{gateway}{path}'
    
    if check_file(fileName) != True:
        return print(f'no file name: {fileName} in {upload_path()}')
    
    upload_directory = upload_path()
    byte = open(os.path.join(upload_directory, fileName), "rb").read(1024)
    encode = base64.b64encode(byte)
    body = encode.decode('ascii')
    
    payload = json.dumps({
        "fileName": f'{fileName}',
        "rawText": json.loads(json.dumps(body, default=str))
    })
    
    file = requests.request("POST", url, headers=headers, data=payload)
    
    return print(file.text)


#url = 'http://google.com/favicon.ico'
#r = requests.get(url, allow_redirects=True)
#open('google.ico', 'wb').write(r.content)
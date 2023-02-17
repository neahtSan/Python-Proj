import requests
import json
import base64
import os
from components.myPath import *
from components.check import *

gateway = ""
payload={}
headers = {'Content-Type': 'application/json'}

#view function return all filename in aws s3 bucket (take no parameter)
def view():
    #define path and combine with url
    path = "/Activity-5-Lambda" 
    url = f'{gateway}{path}'
    
    return print(requests.request("GET", url, headers=headers, data=payload).json())

#get function return download [fileName] file from aws s3 bucket to download directory (take 1 parameter, fileName) 
def get(fileName):
    #define path, payload and combine with url
    path = "/Activity-5-download" 
    url = f'{gateway}{path}'
    payload = json.dumps({
    "fileName": f'{fileName}'
    })
    
    #send POST
    file = requests.request("POST", url, headers=headers, data=payload)
    
    #if error
    if file.status_code != 200:
        return print(file.text)
    
    #handle bytes
    rawText = file.text
    base64_message = bytes(rawText, "utf-8")
    
    #get download directory
    save_directory = download_path()
    
    file_path = os.path.join(save_directory, fileName)
    
    with open(file_path, "wb") as fh:
        fh.write(base64.decodebytes(base64_message))
    
    return print(f'download {fileName} at {save_directory} complete!')

#put function return upload file [fileName] from upload directory to aws s3 bucket (take 1 parameter, fileName) 
def put(fileName):
    #define path and combine with url
    path = "/Activity-5-upload"
    url = f'{gateway}{path}'
    
    #check file in upload directory
    if check_file(fileName) != True:
        return print(f'no file name: {fileName} in {upload_path()}')
    
    #get upload directory
    upload_directory = upload_path()
    
    #handle bytes
    byte = open(os.path.join(upload_directory, fileName), "rb").read(1024)
    encode = base64.b64encode(byte)
    body = encode.decode('ascii')
    
    #define payload
    payload = json.dumps({
        "fileName": f'{fileName}',
        "rawText": json.loads(json.dumps(body, default=str))
    })
    
    #send POST
    file = requests.request("POST", url, headers=headers, data=payload)
    
    return print(file.text)

def newuser(user, password):
    path = "/Activity-6-user"
    url = f'{gateway}{path}'
    payload = json.dumps({
    "user": f'{user}',
    "password":f'{password}'
    })
    
    return print(requests.request("POST", url, headers=headers, data=payload).json())

def login(user, password, login_state):
    path = "/Activity-6-user"
    url = f'{gateway}{path}'
    payload = json.dumps({
    "user": f'{user}',
    "password":f'{password}',
    "image": f'-'
    })
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    if response.text == 'OK':
        login_state = True
        print(response.text)
        return login_state

    return print(response.text)


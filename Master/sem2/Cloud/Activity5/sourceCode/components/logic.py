import requests
import json
import base64
import os
import ast
from datetime import datetime
from components.myPath import *
from components.check import *

gateway = ""
payload={}
headers = {'Content-Type': 'application/json'}

def write_image_access(user, password , image, format_date, size):
    path = "/Activity-6-user"
    url = f'{gateway}{path}'
    payload = json.dumps({
    "user": f'{user}',
    "password": f'{password}',
    "image": f'{user}*{image}',
    "lastModifiedDate": f'{format_date}',
    "size": f'{size}',
    "order": "write_image_access"
    })
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    return print(response.text)

def view_image_access(user, password, all_images):
    path = "/Activity-6-user"
    url = f'{gateway}{path}'
    payload = json.dumps({
    "user": f'{user}',
    "password": f'{password}',
    "image": f'{all_images}',
    "order": "view_image_access"
    })
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    return response

def get_s3_all_file():
    path = "/Activity-5-Lambda" 
    url = f'{gateway}{path}'
    
    list_response = requests.request("GET", url, headers=headers, data=payload).json()
    
    return list_response

#view function return all filename in aws s3 bucket 
def view(user, password):

    list_response = get_s3_all_file()
    
    if type(list_response) == list:
        return print(view_image_access(user, password, list_response).text)
    
    return view_image_access(user, password, list_response).text
    

    
    

#get function return download [fileName] file from aws s3 bucket to download directory (take 1 parameter, fileName) 
def get(fileName, user, password, owner):
    #check image access first
    all_file = get_s3_all_file()
    response = view_image_access(user, password, all_file)
    
    list_response = ast.literal_eval(response.json())
    
    if check_download(list_response, fileName, owner) == 'access grant':
        #define path, payload and combine with url    
        path = "/Activity-5-download" 
        url = f'{gateway}{path}'
        payload = json.dumps({
        "fileName": f'{owner}*{fileName}'
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
    if check_download(list_response, fileName, owner) == False:
        return print(f'User: {user} cannot access to file: {fileName}')
    if check_download(list_response, fileName, owner) == 'wrong owner name':
        return print(f'Wrong owner name: {owner}')
    

#put function return upload file [fileName] from upload directory to aws s3 bucket (take 1 parameter, fileName) 
def put(fileName, user, password):
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
        "fileName": f'{user}*{fileName}',
        "rawText": json.loads(json.dumps(body, default=str))
    })
    
    #send POST
    file = requests.request("POST", url, headers=headers, data=payload)

    #size
    filePath = os.path.join(upload_directory, fileName)
    fileSize = os.path.getsize(filePath)
    
    #modified date
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S+00:00')

    
    #handle table in dynamodb
    if file.status_code == 200:
        write_image_access(user, password, fileName, formatted_date, fileSize)
    
    return print(file.text)

def newuser(user, password):
    path = "/Activity-6-user"
    url = f'{gateway}{path}'
    payload = json.dumps({
    "user": f'{user}',
    "password":f'{password}',
    "image": f'-',
    "order": "newuser"
    })
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    
    return print(response.text)

def login(user, password, login_state):
    path = "/Activity-6-user"
    url = f'{gateway}{path}'
    payload = json.dumps({
    "user": f'{user}',
    "password":f'{password}',
    "image": f'-',
    "order": "login"
    })
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    if response.text == 'OK':
        login_state = True
        print(response.text)
        return login_state

    return print(response.text)

def share(image, shared_user, user, password):
    path = "/Activity-6-user"
    url = f'{gateway}{path}'
    
    s3_file = get_s3_all_file()
    
    payload = json.dumps({
    "user": f'{user}',
    "password":f'{password}',
    "image": f'{user}*{image}',
    "all_image":f'{s3_file}',
    "shared_user":f'{shared_user}',
    "order": "share"
    })
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    return print(response.text)


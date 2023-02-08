import requests
import json

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
    

    r = requests.get(url, allow_redirects=True)
    return open('test.jpg').write(r.content)


#url = 'http://google.com/favicon.ico'
#r = requests.get(url, allow_redirects=True)
#open('google.ico', 'wb').write(r.content)
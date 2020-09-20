import sys
import telnetlib

# http://127.0.0.1:5000/login?data=khaled

HOST = "127.0.0.1"
PORT = "5000"

telnetObj = telnetlib.Telnet(HOST,PORT)
message_GET = ("GET /login?data=idk HTTP/1.1\nHost:"+HOST+"\n\n").encode('ascii')
message_POST = ("POST /login HTTP/1.1\nContent-Length: 235\ndata=idk\nHost:"+HOST+"\n\n").encode('ascii')
telnetObj.write(message_GET) #{'data':'idk really!'}
output = telnetObj.read_all()
#print(output)
telnetObj.close()

"""
url = "http://localhost:8080"
data = {'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data=json.dumps(data), headers=headers)


import requests

url = 'https://bahbah2.com/ws/rest/v1/concept/21f6bb43-98a1-419d-8f0c-8133669e40ca'
data = {"name": "Value"}
r = requests.post(url, auth=('username', 'password'), verify=False, json=data)
print(r.status_code)
"""


"""
mport urllib.request
import json      

body = {'ids': [12, 14, 50]}  

myurl = "http://www.testmycode.com"
req = urllib.request.Request(myurl)
req.add_header('Content-Type', 'application/json; charset=utf-8')
jsondata = json.dumps(body)
jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
req.add_header('Content-Length', len(jsondataasbytes))
print (jsondataasbytes)
response = urllib.request.urlopen(req, jsondataasbytes)
"""




"""
import urllib.request
import json
from pprint import pprint

url = "https://app.close.com/hackwithus/3d63efa04a08a9e0/"

values = {
    "first_name": "Vlad",
    "last_name": "Bezden",
    "urls": [
        "https://twitter.com/VladBezden",
        "https://github.com/vlad-bezden",
    ],
}


headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}

data = json.dumps(values).encode("utf-8")
pprint(data)

try:
    req = urllib.request.Request(url, data, headers)
    with urllib.request.urlopen(req) as f:
        res = f.read()
    pprint(res.decode())
except Exception as e:
    pprint(e)

"""
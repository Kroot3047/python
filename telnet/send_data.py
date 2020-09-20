import requests
import json
from tqdm import tqdm


url = "http://localhost:5000"
data = {'data': 'i dont know really !!'}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
files = {'file1': open('1.png', 'rb')}

r = requests.post(url+"/upload", files=files)
print(requests.ReadTimeout)
#for i in tqdm(range(requests.ReadTimeout)):
#    print(i)

#r = requests.post(url+"/login", data=json.dumps(data).encode('utf-8'), headers=headers)
#r = requests.post(url+"/login", data=data)#, headers=headers)

#r =requests.get(url+"/login"+"?data=i dont know really !!")
#r =requests.get(url+"/login", params=data)

#r_dictionary = r.json()
#print(r) # r.status_code, r.text, r.url
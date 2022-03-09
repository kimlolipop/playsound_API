import requests

url = "http://127.0.0.1:5000/playsound"
id=1
response = requests.get(url+"/"+str(id))
message = response.json()
print(message)
print(response.status_code)
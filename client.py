import requests

url = "http://127.0.0.1:5678/playsound"
sound_name='Money.mp3'
response = requests.get(url+"/"+ sound_name)
message = response.json()
print(message)
print(response.status_code)
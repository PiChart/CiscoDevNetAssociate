import requests
import json

base_url = "https://swapi.dev/api/"
endpoint = "people/"

response = requests.get(base_url + endpoint)
#print(response)
#print("Text")
#print(response.text)
#print("Status Code")
#print(response.status_code)
#print("Headers")
#print(response.headers)

data = response.json()
print(data['results'][0]['name'])  # Print the name of the first character
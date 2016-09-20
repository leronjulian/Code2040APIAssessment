import json, requests

url = "http://challenge.code2040.org/api/haystack"
payload = {"token":"4aaf31adb21e2baeec7768d879744674"}

r = requests.post(url, json = payload)

api_dict = json.loads(r.content.decode('utf-8'))

#Recieves needle from HTTP Request
needle = api_dict['needle']

counter = 0

#Searches for the "Needle in the Haystack
for i in api_dict['haystack']:
    if i == needle:
        break    
    counter += 1

url = "http://challenge.code2040.org/api/haystack/validate"
payload = {"token": "4aaf31adb21e2baeec7768d879744674", "needle":counter}
r = requests.post(url, json = payload)

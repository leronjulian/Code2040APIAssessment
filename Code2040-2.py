import json, requests

url = "http://challenge.code2040.org/api/reverse"
payload = {"token":"4aaf31adb21e2baeec7768d879744674"}

r = requests.post(url, json = payload)

#Reverss the string recieved from the HTTP request
string_to_reverse = r.text
string_reversed = string_to_reverse[::-1]

url = "http://challenge.code2040.org/api/reverse/validate"
payload = {"token":"4aaf31adb21e2baeec7768d879744674","string":string_reversed}
r = requests.post(url, json = payload)

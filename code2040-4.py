import json, requests

url = "http://challenge.code2040.org/api/prefix"
payload = {"token":"4aaf31adb21e2baeec7768d879744674"}

r = requests.post(url, json = payload)

api_dict = json.loads(r.content.decode('utf-8'))

#Gets prefix and strings from the HTTP Request
prefix = api_dict['prefix']
strings = api_dict['array']

strings_without_prefix = []


#Searches for string without the prefix
for a_string in strings:
    if not a_string.startswith(prefix):
        strings_without_prefix.append(a_string)

        
url = "http://challenge.code2040.org/api/prefix/validate"
payload = {"token":"4aaf31adb21e2baeec7768d879744674", "array":strings_without_prefix}
r = requests.post(url, json = payload)

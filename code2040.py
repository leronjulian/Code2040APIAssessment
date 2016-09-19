import requests
import json

token = "ed469c3c9f95a14f27a5d1f6d6363358"
github = "https://github.com/leronjulian/Code2040APIAssessment"
url = "http://challenge.code2040.org/api/register"
payload = json.dumpes({'token' : token, 'github' : github})

r = requests.post(url, payload)
token = json.loads(r.text)["result"]

# =============================================================================
# Stage I: Reverse a string
# =============================================================================

token = "http://challenge.code2040.org/api/reverse"
url = "http://challenge.code2040.org/api/reverse"
payload = json.dumps({'token': token})

r = requests.post(url, payload)
stringToReverse = json.loads(r.text)["result"]

def reverse(string):
    return string[::-1]

string2 = reverse(stringToReverse)

url = "http://challenge.code2040.org/api/reverse/validate"
payload = json.dumps({'token' : token, 'string': string2})

r = requests.post(url, payload)
result = json.loads(r.text)["result"]
print result

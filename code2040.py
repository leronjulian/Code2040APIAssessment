import requests
import json

token = "ed469c3c9f95a14f27a5d1f6d6363358"
github = "https://github.com/leronjulian/Code2040APIAssessment"
url = "http://challenge.code2040.org/api/register"
payload = json.dumpes({'token' : token, 'github' : github})

r = requests.post(url, payload)
token = json.loads(r.text)["result"]

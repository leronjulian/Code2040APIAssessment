import json, requests

url = "http://challenge.code2040.org/api/register"
token = "4aaf31adb21e2baeec7768d879744674"
payload = {"token":"4aaf31adb21e2baeec7768d879744674", "github":"https://github.com/leronjulian/Code2040APIAssessment"}
r = requests.post(url, json = payload)


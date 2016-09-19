import json, requests

url = 'https://github.com/leronjulian/Code2040APIAssessment'
token = '4aaf31adb21e2baeec7768d879744674'
payload = {'token': '4aaf31adb21e2baeec7768d879744674', 'url': 'https://github.com/leronjulian/Code2040APIAssessment'}

response = requests.post(url, data = json.dumps(payload))

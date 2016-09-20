import json, requests, iso8601, time
from datetime import timedelta
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta


url = "http://challenge.code2040.org/api/dating"
payload = {"token": "4aaf31adb21e2baeec7768d879744674"}

r = requests.post(url, json = payload)

api_dict = json.loads(r.content.decode('utf-8'))

# Gets time and date from the HTTP Request
time_interval = int(api_dict['interval'])
datestamp = api_dict['datestamp']

# Parse datestamp and add number of seconds using "dateutil" library
parsed_datestamp = parse(datestamp)
parsed_datestamp += relativedelta(seconds=time_interval)

# Translate to requested format for datestamp
resulting_datestamp = parsed_datestamp.isoformat()[:-6] + "Z"

url = "http://challenge.code2040.org/api/dating/validate"
payload = {"token":"4aaf31adb21e2baeec7768d879744674", "datestamp": resulting_datestamp}
r = requests.post(url, json = payload)

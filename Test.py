import requests
import datetime
resp = requests.post('http://127.0.0.1:5000/attend/teacher/admin/')
attend = resp.json()
for i in attend['present']:
    date =datetime.datetime.strptime(i, '%a, %d %b %Y %H:%M:%S %Z')

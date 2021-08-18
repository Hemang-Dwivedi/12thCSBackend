import requests

url = 'http://127.0.0.1:5000/login/admin/admin123'
resp = requests.get('https://cs-project-database-connection.herokuapp.com//login/admin/admin123').text
print(resp)
if resp == "Success":
    print("YES")
else:
    print(str(resp))

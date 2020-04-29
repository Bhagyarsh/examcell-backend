import requests
import json
url = 'http://127.0.0.1:8000/api/v1/auth/jwt/register'
files = {'dp': open('download.png', 'rb')}
data = {
    "username": "j@J.com",
    "first_name": "jay",
    "last_name": "dhumal",
    "password": "bhagyarsh31",
    "parents": False,
    "student": True,
    "staff": False
}
r = requests.post(url,data=data ,files=files)
print(r.status_code)
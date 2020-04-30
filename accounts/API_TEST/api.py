import requests
import json
url = 'http://127.0.0.1:8000/api/v1/auth/jwt/register'
urllogin = 'http://127.0.0.1:8000/api/v1/auth/jwt'
# files = {'dp': open('download.png', 'rb')}
# data = {
#     "Username": "j@Jdasdfsdddfsd.com",
#     "first_name": "jay",
#     "last_name": "dhumal",
#     "password": "bhagyarsh31",
#     "parents": False,
#     "student": True,
#     "staff": False
# }
# r = requests.post(url,data=data ,files=files)
# print(r.content)
# # print(r.content)
# print(r.status_code)

data = {
    "username": "bhagyarsh@gmail.com",
    "password": "bhagyarsh31"
}
header = {

}
r = requests.post(url=urllogin,json=data)
print(r)
print(r.content)
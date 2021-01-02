import requests
from bs4 import BeautifulSoup as bs


s = requests.session()

csrf_token = s.get(URL).cookies["_kjb_session"]

data = {
    "authenticity_token": csrf_token,
    "member[email]": "angara99@gmail.com",
    "member[password]": "suki33338",
}

res = s.post(URL_LOGIN, headers=HEADERS, data=data)
print(res)

import requests
from bs4 import BeautifulSoup as bs


URL = "https://www.englishcoachchad.com"
URL_LOGIN = "https://www.englishcoachchad.com/login"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "origin": URL,
    "referer": URL_LOGIN,
}


s = requests.session()

csrf_token = s.get(URL).cookies["_kjb_session"]

data = {
    "authenticity_token": csrf_token,
    "member[email]": "angara99@gmail.com",
    "member[password]": "suki33338",
}

res = s.post(URL_LOGIN, headers=HEADERS, data=data)
print(res)

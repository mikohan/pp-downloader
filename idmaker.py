from bs4 import BeautifulSoup as bs
import requests
from requests.auth import HTTPBasicAuth
import re
import werkzeug

werkzeug.cached_property = werkzeug.utils.cached_property
from robobrowser import RoboBrowser

credentials = ("angara99@gmail.com", "suki33338")
# data = {"login": "angara99@gmail.com", "password": "suki33338"}
url_login = "https://www.englishcoachchad.com/login"


url_course = (
    "https://www.englishcoachchad.com/products/practice-paradise/categories/553711"
)

browser = RoboBrowser()

browser.open(url_login)

signup_form = browser.get_form(id="new_member_session")
print(signup_form)
signup_form["member[email]"].value = "angara99@gmail.com"

signup_form["member[password]"].value = "suki33338"
browser.submit_form(signup_form)

content = browser.parsed()
prit(content)

f = open("tmp.html")
f.write(content, "w")
f.close()

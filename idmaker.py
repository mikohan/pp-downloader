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
user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"


url_course = (
    "https://www.englishcoachchad.com/products/practice-paradise/categories/553711"
)

browser = RoboBrowser(user_agent=user_agent, parser="lxml")

browser.open(url_login)

signup_form = browser.get_form(id="new_member_session")
print(signup_form)
signup_form["member[email]"].value = "angara99@gmail.com"

signup_form["member[password]"].value = "suki33338"
browser.submit_form(signup_form)
browser.follow_link(browser.get_link(url_course))

content = browser.parsed()

with open("tmp.html", "w") as f:
    f.write(sr(content))

from bs4 import BeautifulSoup as bs
import requests
from requests.auth import HTTPBasicAuth
import re
from robobrowser import RoboBrowser

credentials = ("angara99@gmail.com", "suki33338")
# data = {"login": "angara99@gmail.com", "password": "suki33338"}
url_login = "https://www.englishcoachchad.com/login"


url_course = (
    "https://www.englishcoachchad.com/products/practice-paradise/categories/553711"
)

browser = RoboBrowser(username="angara99@gmail.com", password="suki33338")

browser.open(url_login)

signup_form = browser.get_form("login_form")
signup_form["identity"].value = self.username

signup_form["password"].value = self.password
browser.submit_form(signup_form)

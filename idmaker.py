from bs4 import BeautifulSoup as bs
import requests
from requests.auth import HTTPBasicAuth
import re
from linkParser import get_video_id
import csv
from config import PASS, USER, URL
import os

re._pattern_type = re.Pattern
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
signup_form["member[email]"].value = USER

signup_form["member[password]"].value = PASS
browser.submit_form(signup_form)
browser.open(url_course)

content = browser.parsed()
browser.find_all("div", class_="syllabus__item")
links = browser.get_links()

append: str = "w"
if os.path.exists("links.txt"):
    append = "a"
else:
    append = "w"

with open("links.txt", append) as file:
    for link in links:
        file.write(str(link.get("href")) + "\n")
        print(link.get("href"))

# Here will be loop for finded liks


# Write to csv file

with open("video_ids.csv", "a") as csv:
    # loop here
    pass

with open("tmp.html", "w") as f:
    f.write(str(content))

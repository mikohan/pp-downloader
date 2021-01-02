from bs4 import BeautifulSoup as bs
import requests
from requests.auth import HTTPBasicAuth
import re
from linkParser import get_video_id
import csv
from config import PASS, USER, URL
import os
import time

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
signup_form["member[email]"].value = USER
signup_form["member[password]"].value = PASS
browser.submit_form(signup_form)
print("Form submited")

browser.open(url_course)
content = browser.parsed()
# browser.find_all("div", class_="syllabus__item")
# links = browser.get_links()
print("Getting content")

soup = bs(str(content), "lxml")

raw_divs = soup.find_all("div", class_="syllabus__item")
print(len(raw_divs), "Before set")
uniq_divs = set(raw_divs)
print(len(uniq_divs), "unuque divs")
divs = list(uniq_divs)


append: str = "w"
if os.path.exists("links.txt"):
    append = "a"
else:
    append = "w"

print("Starting collecting rows")

with open("links.txt", append) as file:
    for (i, div) in enumerate(divs):
        time.sleep(1)
        single_link = str(URL) + str(div.a["href"])
        title = div.find("p", class_="syllabus__title")

        browser.open(single_link)
        page_html = str(browser.parsed())

        s = bs(page_html, "lxml")
        d = s.find("div", class_="wistia_embed")
        m = re.search('(wistia_async_)(\w+)"', str(d))
        id = str(m.group(2))

        row = (
            str(i + 1).zfill(5)
            + " - "
            + str(title.text).replace(",", ";")
            + ","
            + str(id)
            + "\n"
        )
        file.write(row)
        print(row)

# 1 - First Lesson Shadowing,hi7s2ot6qa
# Here will be loop for finded liks


# Write to csv file

with open("tmp.html", "w") as f:
    f.write(str(content))

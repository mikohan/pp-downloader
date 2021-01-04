import sys
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
try:
    url_course = str(sys.argv[1])
    title_course = str(sys.argv[2]).replace(" ", "_")
    print("------------------")
    print("args passed...")

except:
    sys.exit("Pass course url and course title please")

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
divs = []
for rd in raw_divs:
    if rd not in divs:
        divs.append(rd)
print(len(divs), "unuque divs")


append: str = "w"
if os.path.exists(str(title_course) + ".csv"):
    append = "a"
else:
    append = "w"


print("Starting collecting rows")

with open(title_course + ".csv", append) as file:
    if append == "w":
        file.write("Video_Title,vid_id" + "\n")

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
            '"'
            + str(i + 1).zfill(5)
            + " - "
            + str(title.text).replace(",", ";").replace("/", "")
            + '"'
            + ","
            + str(id)
            + "\n"
        )
        file.write(row)
        print(row)
        # Comment for git hub

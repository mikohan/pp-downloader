import requests
from bs4 import BeautifulSoup as bs

html = open("tmp.html", r)
soup = bs(html, "lxml")

divs = soup.find_all("div", "syllabus__item")

for div in divs:
    print(div.a("href"))

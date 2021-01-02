import requests
from bs4 import BeautifulSoup as bs

html = open("tmp.html", "r")
soup = bs(html, "lxml")

divs = soup.find_all("div", class_="syllabus__item")

for div in divs:
    title = div.find("p", class_="syllabus__title")
    print(title)

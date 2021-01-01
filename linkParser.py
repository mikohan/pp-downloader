from bs4 import BeautifulSoup as bs
import requests
import re

from request_test import URL

with open("tmp.html", "r") as html:
    soup = bs(html, "html.parser")
    # divs_all = soup.find_all("div", class_="syllabus__item")
    f = open("single_page.html", "r")
    content = f.read()
    s = bs(content, "lxml")
    d = s.find("div", class_="wistia_embed")
    m = re.search('(wistia_async_)(\w+)"', str(d))
    print(m.group(2))

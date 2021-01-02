from bs4 import BeautifulSoup as bs
import requests
import re

from request_test import URL


def get_video_id(url: str, headers: dict) -> str:

    r = requests.get(url, headers)
    html = r.text

    soup = bs(html, "lxml")
    # divs_all = soup.find_all("div", class_="syllabus__item")
    f = open("single_page.html", "r")
    content = f.read()
    s = bs(content, "lxml")
    d = s.find("div", class_="wistia_embed")
    m = re.search('(wistia_async_)(\w+)"', str(d))
    print(m.group(2))
    return m.group(2)

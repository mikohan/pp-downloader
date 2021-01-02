from bs4 import BeautifulSoup as bs
import requests
import re

from config import URL, HEADERS


def get_video_id(url: str, HEADERS: dict) -> str:

    r = requests.get(url, headers)
    html = r.text

    soup = bs(html, "lxml")
    # divs_all = soup.find_all("div", class_="syllabus__item")
    f = open("single_page.html", "r")
    content = f.read()
    s = bs(content, "lxml")
    d = s.find("div", class_="wistia_embed")
    m = re.search('(wistia_async_)(\w+)"', str(d))
    print("in get video function", m.group(2))
    return m.group(2)

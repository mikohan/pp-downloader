from bs4 import BeautifulSoup as bs
import requests
import re

from config import URL, HEADERS


def get_video_id(url: str) -> str:

    r = requests.get(str(url), headers=HEADERS)
    html = r.text
    print(html)

    s = bs(html, "lxml")
    d = s.find("div", class_="wistia_embed")
    print(d)
    m = re.search('(wistia_async_)(\w+)"', str(d))
    return m.group(2)

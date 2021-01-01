from bs4 import BeautifulSoup as bs


with open("tmp.html", "r") as html:
    soup = bs(html, "html.parser")
    divs_all = soup.find_all("div", class_="syllabus__item")
    for div in divs_all:
        print(div.a["href"])

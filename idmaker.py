from bs4 import BeautifulSoup as bs
import requests

url = "https://www.englishcoachchad.com/products/practice-paradise/categories/553711"

r = requests.get(url)
print(r.status_code)

html = r.text
print(html)

# soup = bs(html, "html.parser")

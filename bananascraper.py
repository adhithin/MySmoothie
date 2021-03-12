import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/Banana'

headers = { "User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="firstHeading").get_text()

print(title)

print(URL)
import requests
from bs4 import BeautifulSoup

url = "https://www.circlek.lv/"
response = requests.get(url)
# izveido objektu
soup = BeautifulSoup(response.content, 'html.parser')

# atrodi virsrakstu elementu
title = soup.find("title")
print(title.text)
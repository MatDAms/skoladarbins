import requests
from bs4 import BeautifulSoup
# ziņu lapa
url = "https://www.delfi.lv"
# veicam  http get pieprasījumu
resp = requests.get(url)
# izveidojam objektu
soup = BeautifulSoup(resp.text,'html.parser')
# atrodam visus virsrakstus
headlines = soup.find_all( class_='headline')
# izvadam virsraskt
print('virsrakst')
for headline in headlines:
    print(headline.text.strip())


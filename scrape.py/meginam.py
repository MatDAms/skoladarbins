from bs4 import BeautifulSoup
# html pamats
html_lapa = "<html><body><h1>Hello, World!</h1></body></html>"
# izveidojam objektu
soup = BeautifulSoup(html_lapa, 'html.parser')
#iegūsma tekstu no h1 elementa
text = soup.h1.text
# izvadam rezultātu
print("teksts:", text)
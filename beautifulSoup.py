from urllib.request import urlopen
from bs4 import BeautifulSoup
content = urlopen("http://testing-ground.scraping.pro/blocks")
soup = BeautifulSoup(content.read(),"lxml")
print(soup.h1)


from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')

bs = BeautifulSoup(html, 'html.parser')

nameList = bs.findAll('span', {'class': 'green'})  #findAll : 페이지의 태그 전체
for name in nameList:
    print(name.get_text())
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen('http://pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The suerver could not be found!')

bs = BeautifulSoup(html.read(), 'html.parser')
# bs = BeautifulSoup(html.read(), 'lxml')  # 지저분한 html 코드를 분석할 때

print(bs.h1)


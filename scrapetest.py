from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle('https://www.google.com/search?q=%EB%9D%BC%EC%BD%94%EC%8A%A4%ED%85%8C+%EA%B0%80%EB%94%94%EA%B1%B4&oq=%EB%9D%BC%EC%BD%94%EC%8A%A4%ED%85%8C+%EA%B0%80%EB%94%94%EA%B1%B4&aqs=chrome.0.0i512l7j69i60.2192j0j4&sourceid=chrome&ie=UTF-8')
if title == None:
    print('Title could not be found')
else:
    print(title)
from urllib.request import urlopen
import ssl
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Emilia.html'

i = 8
while i != 0:
    print(url)
    html = urlopen(url, context = ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    links = list()
    for tag in tags:
        links.append(tag.get('href', None))
    i = i - 1
    url = links[17]

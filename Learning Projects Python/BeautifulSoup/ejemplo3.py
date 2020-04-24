from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url='http://py4e-data.dr-chuck.net/comments_380961.html'

html = urlopen(url, context=ctx).read()
soup=BeautifulSoup(html, 'html.parser')
tags=soup.find_all('span', class_='comments')
suma=0
for tag in tags:
    suma+=int(tag.text)

print (suma)
    


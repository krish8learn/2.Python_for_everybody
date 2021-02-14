#opening a webpage through parsing of beautiful soup for HTML
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
url="http://py4e-data.dr-chuck.net/comments_42.html"
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')
print(soup)

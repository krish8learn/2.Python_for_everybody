#opening the webpage then parsing it's HTML elements by beaautiful soup then printing desired item by using built in method of beautiful soup
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
url = 'http://www.dr-chuck.com/page1.htm'
fhand = urllib.request.urlopen(url).read()
soup = BeautifulSoup(fhand, 'html.parser')
#to retrieve all the anchor/<a> tags
tags = soup('a')
for tag in tags:
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)

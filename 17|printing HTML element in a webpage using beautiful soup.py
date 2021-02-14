#opening webpage through beautiful soup, then printing certain HTML element
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
fhand= input("Enter url: ")
url = fhand
file = urllib.request.urlopen(url).read()
soup = BeautifulSoup(file,'html.parser')
# retrieving the span (<span>) tags
sum = 0
count =0
tags = soup('span')
for tag in tags:
    #print(tag.contents[0])
    count+=1
    sum = sum + int(tag.contents[0])
print("count ",count)
print('sum ',sum)

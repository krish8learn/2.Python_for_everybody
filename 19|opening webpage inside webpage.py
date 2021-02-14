#opening webpages inside the webpages
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
count = int(input("Enter number of repeatation you want: "))
pos = int(input("Which position to repeat: "))
link = input("Enter url: ")
print("Working on ", link)

for i in range(count):
    file = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(file,'html.parser')
    tags = soup('a')
    link = tags[pos-1].get('href')

print(tags[pos-1].contents[0])

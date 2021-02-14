#webpage has xml data so opening the page, then parsing the element and performing sum on specific element
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

link = input("Enter URL: ")
address = urllib.request.urlopen(link).read()
print("Retrieving",link)
print('Retrieved',len(address),'characters')
tree = ET.fromstring(address)
deep = tree.findall('comments/comment')
print(len(deep))
sum =0;
for item in deep:
    sum = sum + int(item.find('count').text)
print("sum: ",sum)

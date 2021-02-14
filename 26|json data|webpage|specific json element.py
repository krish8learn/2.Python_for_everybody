#json data in a webpage, performing summation with a specific elements
import urllib.request, urllib.parse, urllib.error
import json

address = input("Enter the url: ")
print("Retrieving url", address)
fhandle = urllib.request.urlopen(address) #open the urlopen
data = fhandle.read().decode()            #url is converted from utf-8 to unicode
print("Retrived:",len(data),"characters")

js = json.loads(data)

sum =0

print("Total count:",len(js))
print("Total count:",len(js["comments"]))
for item in js["comments"]:
    sum = sum + int(item["count"])
print("sum:",sum)

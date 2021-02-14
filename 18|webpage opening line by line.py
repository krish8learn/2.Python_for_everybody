#opening a webpage line by line using for loop
import urllib.request, urllib.parse, urllib.error
fhand = input("Enter url ")
file = urllib.request.urlopen(fhand)
for line in file:
    data = line.decode().strip()
    print(data)

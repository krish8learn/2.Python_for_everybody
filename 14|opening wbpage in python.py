#Here, we re opening a web page in python
import urllib.request, urllib.error, urllib.parse
fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_912677.html')
for line in fhand:
    data = line.decode().strip()
    print(data)
#http://py4e-data.dr-chuck.net/comments_42.html
#http://www.dr-chuck.com/page1.htm
#http://py4e-data.dr-chuck.net/comments_912677.html

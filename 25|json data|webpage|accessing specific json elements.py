# json data inside a webpage
import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/json?'

while True:
    address = input("Enter Location: ")
    if len(address)<1 or address =="EXIT":
        break
    url = serviceurl + urllib.parse.urlencode({'address':address})
    print("Retrieving url: ",url)
    fhandle = urllib.request.urlopen(url)
    data = fhandle.read().decode()
    print("Retrieved:",len(data),"characters")

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status']!='OK':
        print("Failure")
        print(data)
        continue
    print(json.dumps(js,indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat',lat,'lng',lng)
    location = js['results'][0]['formatted_address']
    print(location)

#importing required libraries
import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import ssl
import time
import sys

api_key = False
#for google api, api_key = "AIzaSy______IDByT70"

#now we would try to use either Dr.Chuck provided api or Google api
if api_key is False:
    serviceurl = "http://py4e-data.dr-chuck.net/geojson?"
else:
    serviceurl = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

#now we will create a database file
conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)
''')

#now we are gonna open the file all data are written
fhandle = open("where.data")
#NOW WE WILL STORE THE RAW JSON DATA WHICH IS address CORRESPOND TO THE NAME IN where.data
count = 0
for line in fhandle:
    if count > 200:
        print("Retrieved 200 Locations.")
        break
    address = line.strip() # we are gonna remove the spaces from every lines
    cur.execute("SELECT geodata FROM Locations WHERE address = ?",(memoryview(address.encode()),))
#purpose of the encode() is convert the unicode data address into utf
#purpose of below code is to check if the address already in the database, if present then continue to next one, if not present then store in data
     try:
         data = cur.fetchone()[0]
         print("Present in database",address)
         continue
     except:
         pass
#next paragraph code related to api_key verification regarding google api
    parms = dict()
    parms["query"] = address
    if api_key is not False: parms['key'] = api_key
#performing search operations
    url = serviceurl + urllib.parms.urlencode(parms)

    print("Retreiving URL",url)
    uh = urllib.request.urlopen(url,context=ctx)
    #converting data into unicode
    data = uh.read().decode()
    print('Retrived',len(data),'characters', data[:20].replace('\n',' '))
    count = count + 1


#parsing json data from that website
    try:
        js = json.loads(data)
    except:
        print(data)
        continue
#a 'Status' is present in the json data indicates the condition of JSON
    if 'status' not in js or (js['status'] !='OK' and js ['status'] !='ZERO_RESULTS'):
        print('---FAIL TO Retrive---')
        print(data)
        break

    cur.execute('''INSERT INTO Locations (address,geodata) VALUES(?,?)''',(memoryview(address.encode()),memoryview(data.encode())))
    conn.commit()

print("Run geodump.py to read the data from the database so you can vizualize it on a map.")
        

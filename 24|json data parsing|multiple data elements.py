# parsing json of multiple main elements
import json
data = '''[
{ "id":"01",
  "x":"08",
  "name":"Krish"
},
{ "id":"02",
  "x":"04",
  "name":"Sumana"
}
]'''
info = json.loads(data)
print("User count:",len(info))
for item in info:
    print("Name: ",item["name"])
    print("x:",item["x"])
    print("id: ",item["id"])

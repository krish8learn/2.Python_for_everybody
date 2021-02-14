#json data parsing
import json
data = '''{
"name":"Krish",
"phone":{
"type": "int",
"number": "8240903775"
},
"email":{
"hide":"yes"
}
}'''
info = json.loads(data)
print("Name: ",info["name"])
print("Number: ",info["phone"]["number"])
print("Email attr: ",info["email"]["hide"])

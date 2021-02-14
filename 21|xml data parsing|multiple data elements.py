#xml data parsing of multiple main elements
import xml.etree.ElementTree as ET
data = '''<stuff>
<users>
<user x='1'>
<id>008</id>
<name>Krish</name>
</user>
<user x='2'>
<id>004</id>
<name>Sumana</name>
</user>
</users>
</stuff>'''
input = ET.fromstring(data)
usr = input.findall('users/user')
print("user count: ",len(usr))
for item in usr:
    print("Name: ",item.find('name').text)
    print("Id: ",item.find('id').text)
    print("Attr: ",item`.get('x'))

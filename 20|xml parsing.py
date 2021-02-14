#parsing xml data
import xml.etree.ElementTree as ET
data = '''<person>
<name>Krish</name>
<phone type='intl'>8240903775</phone>
<email hide ='yes'>krishkarmakar17@gmail.com</email>
</person>'''
tree = ET.fromstring(data)
print("Name: ",tree.find('name').text)
print("Email Attribute: ",tree.find('email').get('hide'))
print("Email: ",tree.find('email').text)
print("Phone: ",tree.find('phone').text)
print("Phone Attribute: ",tree.find('phone').get('type'))

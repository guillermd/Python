import xml.etree.ElementTree as ET 

data = '''<person>
<name>Chuck</name>
<phone type= "intl">+34636533128</phone>
<email hide="yes"/>
<name>John</name>
<phone type= "intl">+34915001190</phone>
<email hide="no"/></person>'''

tree=ET.fromstring(data)

print('Name: ',tree.find('name').text) #Devuelve el valor del campo
print('Name: ',tree.find('email').get('hide')) #get() Devuelve el valor del atributo
list=tree.findall('name')

for l in list:
    print (l.text)
    

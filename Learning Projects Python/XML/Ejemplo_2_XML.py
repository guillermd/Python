import xml.etree.ElementTree as ET 

data = '''<stuff>
<users>
    <user x="6">
        <id>001</id>
        <name>Chuck</name>
    </user>
    <user x="7">
        <id>002</id>
        <name>John</name>
    </user>
</users>
</stuff>'''

stuff= ET.fromstring(data)
lst=stuff.findall('users/user')
print('Usuarios: ', len(lst))
for l in lst:
    print('Name', l.find('name').text)
    print('Id', l.find('id').text)
    print('Attribute', l.get('x'))
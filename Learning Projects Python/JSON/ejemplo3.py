import urllib.request, urllib.parse, urllib.error
import json

url = 'http://py4e-data.dr-chuck.net/comments_380964.json'    
    
print('Retrieving ', url)
uh=urllib.request.urlopen(url)
data=uh.read().decode()
print('Retrieved ', len(data), 'characters')
info=json.loads(data)
print("Count:", len(info))
total=0
for item in info["comments"]:
    try:
        total+=int(item['count'])
    except ValueError:
        print("Este valor no es un numero")
        pass 
    
print("Sum:",total)
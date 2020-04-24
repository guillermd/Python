import json

data = '''{"name":"Chuck", "phone":{"type":"intl", "number":"+34 636 533 128"}, "email":{"hide":"yes"}}'''

info=json.loads(data)
print('Name:', info["name"])
print('Email:', info["email"]["hide"])
print('Phone:', info["phone"]["number"], "Type:", info["phone"]["type"], )
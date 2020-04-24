import json

data = '''[{"id":"001", "x":"2", "name":"chuck"}
          ,{"id":"002", "x":"3", "name":"Andy"}]'''

info=json.loads(data)
print("items:", len(info))
for i in info:
    print('Name:', i["name"])
    print('Id:', i["x"])
    print('X:', i["x"])
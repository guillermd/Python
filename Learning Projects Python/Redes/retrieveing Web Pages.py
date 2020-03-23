import urllib.request, urllib.error, urllib.parse
#la libreria urllib hace el trabajo del socket y nos muestra el contedio web como un fuichero

fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts=dict()

for li in fhand:
    words=li.decode().split()
    for w in words:
        counts[w]=counts.get(w,0)+1
print (counts)


print(ord('L'))


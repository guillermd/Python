from bs4 import BeautifulSoup
import requests
import pandas as pd

url='https://resultados.as.com/resultados/futbol/segunda/clasificacion'
page = requests.get(url)
soup=BeautifulSoup(page.content, 'html.parser')

#Equipos
eq=soup.find_all('span', class_='nombre-equipo')
equipos=list()
count=0
for i in eq:
    if(count<22):
        equipos.append(i.text)
        count+=1
    else:
        break

#Puntos
pt=soup.find_all('td', class_='destacado')
puntos=list()
countPt=0
for p in pt:
    if(countPt<22):
        puntos.append(p.text)
        countPt+=1
    else:
        break

df=pd.DataFrame({'Nombre':equipos, 'Puntos': puntos}, index=list(range(1,23)))
print (df)
df.to_csv('Clasificiacion.csv', index=False)

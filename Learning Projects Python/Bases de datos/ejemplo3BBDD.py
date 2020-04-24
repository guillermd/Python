import sqlite3
#En esta pagina se puede ir viendo los cambios de base de datos. https://sqliteonline.com/ no se ven los cambios en caliente, hay que darle el fichero cada vez

#LEER REGISTROS
miConexion=sqlite3.connect("PrimeraBase")
miCursor=miConexion.cursor()
miCursor.execute("SELECT * FROM PRODUCTO")
variosProd=miCursor.fetchall() #Devuelve una lista con todos los registros qeu nos devuelve el select
print("fetchall: ",variosProd)
print("-------------------------")
for p in variosProd:
    print(p)
    print("Solo el primer elemento de la tupla: ",p[0])


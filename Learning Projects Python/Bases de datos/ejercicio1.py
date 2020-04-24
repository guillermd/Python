import sqlite3
#crear clave primaria en la tabla
miConexion=sqlite3.connect("coursera")
miCursor=miConexion.cursor()

#miCursor.execute('''
#    CREATE TABLE Ages ( 
#  name VARCHAR(128), 
#  age INTEGER
#)
#''')
#con la clausula UNIQUE evitamos q la tabla tenga ese campo con el mismo contenido mas de una vez

#variosProductos=[('Salahudin', 38), ('Zaynab', 27), ('Dhara', 19),('Chantelle', 22)]

miCursor.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X') 
variosProd=miCursor.fetchall() #Devuelve una lista con todos los registros qeu nos devuelve el select
print(variosProd)
miConexion.commit()
miConexion.close()

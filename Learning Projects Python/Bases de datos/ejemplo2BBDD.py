import sqlite3
#En esta pagina se puede ir viendo los cambios de base de datos. https://sqliteonline.com/ no se ven los cambios en caliente, hay que darle el fichero cada vez
#abrir conexion
miConexion=sqlite3.connect("PrimeraBase")
#crear puntero o cursor
miCursor=miConexion.cursor()
#manejar resultados
variosProductos=[
    ("BALON", 10, "DEPORTES"), ("CAMION", 17, "JUGUETES"), ("BOMBILLA", 21, "ELECTRICIDAD")
]

miCursor.executemany("INSERT INTO PRODUCTO VALUES (?,?,?)", variosProductos) #EJECUTA LA ACCION SOBRE UNA LISTA DE ELEMENTOS

miConexion.commit()
#cerrar puntero
#miCursor.close()
#cerrar conexion
miConexion.close()

#LEER REGISTROS
miConexion2=sqlite3.connect("PrimeraBase")
miCursor2=miConexion2.cursor()
miCursor2.execute("SELECT * FROM PRODUCTO")
variosProd=miCursor2.fetchall() #Devuelve una lista con todos los registros qeu nos devuelve el select
print(variosProd)

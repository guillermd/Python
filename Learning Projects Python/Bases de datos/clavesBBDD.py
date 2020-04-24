import sqlite3
#crear clave primaria en la tabla
miConexion=sqlite3.connect("GestionProductos")
miCursor=miConexion.cursor()

miCursor.execute('''
    CREATE TABLE PRODUCTO (ID INTEGER PRIMARY KEY AUTOINCREMENT , NOMBRE_ARTICULO VARCHAR(30) UNIQUE, PRECIO INT, SECCION VARCHAR(15))
''')
#con la clausula UNIQUE evitamos q la tabla tenga ese campo con el mismo contenido mas de una vez

variosProductos=[
    ("BALON", 10, "DEPORTES"), ("CAMION", 17, "JUGUETES"), ("BOMBILLA", 21, "ELECTRICIDAD")
]

miCursor.executemany("INSERT INTO PRODUCTO VALUES (NULL,?,?,?)", variosProductos) 
miConexion.commit()
miConexion.close()
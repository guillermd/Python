import sqlite3
miConexion=sqlite3.connect("BBBDDCrud")
miCursor=miConexion.cursor()

variosProductos=[
    ("BALON", 10, "DEPORTES"), ("CAMION", 17, "JUGUETES"), ("BOMBILLA", 21, "ELECTRICIDAD")
]
miCursor.execute("CREATE TABLE PRODUCTO (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE_ARTICULO VARCHAR(30), PRECIO INT, SECCION VARCHAR(15))")
miCursor.executemany("INSERT INTO PRODUCTO VALUES (null, ?,?,?)", variosProductos)
miConexion.commit()

#UPDATE
miCursor=miConexion.cursor()
miCursor.execute("update producto set precio = 55 where precio = 10")
miConexion.commit()
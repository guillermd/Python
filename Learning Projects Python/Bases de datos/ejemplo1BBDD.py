import sqlite3
#En esta pagina se puede ir viendo los cambios de base de datos. https://sqliteonline.com/ no se ven los cambios en caliente, hay que darle el fichero cada vez
#abrir conexion
miConexion=sqlite3.connect("PrimeraBase")
#crear puntero o cursor
miCursor=miConexion.cursor()
#manejar resultados
#miCursor.execute("CREATE TABLE PRODUCTO (CODIGO_PRODUCTO VARCHAR(5) PRIMARY KEY NOMBRE_ARTICULO VARCHAR(30), PRECIO INT, SECCION VARCHAR(15))")
#miCursor.execute("INSERT INTO PRODUCTO VALUES('FRESON HUELVA', 35, 'FRUTERIA')")
miCursor.execute("DELETE FROM PRODUCTO WHERE NOMBRE_ARTICULO LIKE 'FRESA'")
miConexion.commit()
#cerrar puntero
#miCursor.close()
#cerrar conexion
miConexion.close()
#con el asterisco indicamos que no sabemos el numero de argumentos que va a recibir y esos argumentos los recibirá en forma de tupla
def devuelveCiudades(*ciudades):
    for i in ciudades:
       #for subItem in i:
            #yield subItem
        yield from i #hace un for anidado

ciudadesGeneradas=devuelveCiudades("madrid", "pinto", "parla")

print (next(ciudadesGeneradas))
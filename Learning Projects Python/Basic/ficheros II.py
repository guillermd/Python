#Fases-> Creacion, Apertura, Manipulación, Cierre

from io import open

class Ejemplo1():
    def EjecutarEjemplo(self):
        archivo_texto=open("archivo.txt", "r") 
        print(archivo_texto.read()) #el puntero se queda al final del fichero
        archivo_texto.seek(4) #coloca el puntero en esta posicion. NO LEE
        print(archivo_texto.read())        
    
class Ejemplo2():
    def EjecutarEjemplo(self):
        archivo_texto=open("archivo.txt", "r") 
        print(archivo_texto.read(15))#lectura hasta del caracter 15
        print(archivo_texto.read()) #Lee a partir de donde tiene el puntero, 15 en este caso

class Ejemplo3():
    def EjecutarEjemplo(self):
        archivo_texto=open("archivo.txt", "r") 
        archivo_texto.seek(len(archivo_texto.read())/2)
        print(archivo_texto.read())

class Ejemplo4():
    def EjecutarEjemplo(self):
        archivo_texto=open("archivo.txt", "r") 
        archivo_texto.seek(len(archivo_texto.readline()))#puntero situado al final de la primera linea
        print(archivo_texto.read())

class Ejemplo5():
    def EjecutarEjemplo(self):
        archivo_texto=open("archivo.txt", "r+") #apertura en modo lectura y escritura
        archivo_texto.write("comienzo del text2") #se ecribe al principio del fichero, machacando lo que hubiera y deja el cursor en esa posicion
        archivo_texto.seek(0)
        print(archivo_texto.read())

class Ejemplo6():
    def EjecutarEjemplo(self):
        archivo_texto=open("archivo.txt", "r+") #apertura en modo lectura y escritura
        lineas=archivo_texto.readlines()
        lineas[1]="Esta linea incluida desde el exterior \n"        
        archivo_texto.seek(0)
        archivo_texto.writelines(lineas)
        archivo_texto.seek(0)
        print(archivo_texto.read())
        archivo_texto.close()

Ej=Ejemplo6()
Ej.EjecutarEjemplo()



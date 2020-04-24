#Fases-> Creacion, Apertura, Manipulación, Cierre

from io import open

class Nuevo_Fichero():
    def EjecutarEjemplo(self):
        #modo escritura
        archivo_text=open("archivo.txt", "w")#w modo lectura, si no existe el ficheor, lo crea
        frase="una frase para mi archivo \nSegunda linea"
        archivo_text.write(frase)
        archivo_text.close()

class Lectura_Fichero():
    def EjecutarEjemplo(self):    
        archivo_text=open("archivo.txt", "r") #modo lectura
        texto=archivo_text.read()
        print(texto)
        archivo_text.close()

class Lectura_Fichero_Lineas():
    def EjecutarEjemplo(self):  
        archivo_text=open("archivo.txt", "r")
        texto=archivo_text.readlines() #lee la informacion linea a linea, y lo incluye en una lista.
        print(texto)
        print(texto[0])
        archivo_text.close()

class Append_Fichero():
    def EjecutarEjemplo(self):  
        #agregar lineas al fichero
        archivo_text=open("archivo.txt", "a") #append
        archivo_text.write("\n Tercera linea del fichero")
        archivo_text.close()
        archivo_text=open("archivo.txt", "r")
        texto=archivo_text.read()
        archivo_text.close()
        print(texto)

Ej=Lectura_Fichero()
Ej.EjecutarEjemplo()


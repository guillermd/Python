#biblioteca Pickle
#Metodo dump().- volcar datos al fichero binario externo
#Metodo load().- carga de datos del fichero binario externo
import pickle

class CrearFichero():
    def Ejecutar_Ejemplo(self):
        lista_nombres=["pepe", "ana", "luis", "isabel"]
        fichero_binario=open("nombres2", "wb") #wb=> Escritura binaria
        pickle.dump(lista_nombres, fichero_binario)
        fichero_binario.close()
        del(fichero_binario)#Borra de la memoria el fichero binario con el que hemos trabajado

class LeerFichero():
    def Ejecutar_Ejemplo(self):
        fichero=open("lista_nombres", "rb") #wb=> Lectura binaria
        lista=pickle.load(fichero)
        print(lista)

Ej=CrearFichero()
Ej.Ejecutar_Ejemplo()

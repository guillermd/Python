import pickle
#creamos el objeto a serializar
class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enMarcha=False
        self.acelera=False
        self.frena=False
    
    def arrancar(self):
        self.enMarcha=True

    def acelerar(self):
        self.acelera=True
    
    def frenar(self):
        self.frena=True
    
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEnMarcha: ", self.enMarcha, 
                "\nAcelera: ", self.acelera, "\nFrena:", self.frena)

class Serializar_Objetos:
    def Ejecutar_Ejemplo(self):
        coche1=Vehiculos("ford","fiesta")
        coche2=Vehiculos("seat","leon")
        coche3=Vehiculos("opel","corsa")
        coches=[coche1,coche2, coche3]

        fichero=open("lista_coches", "wb")
        pickle.dump(coches, fichero)
        fichero.close()
        del(fichero)

class Deserializar_Objetos:
    def Ejecutar_Ejemplo(self):
        fichero=open("lista_coches", "rb")        
        misCoches=pickle.load(fichero)
        for c in misCoches:
            print(c.estado())
        fichero.close()
        del(fichero)

Ej=Deserializar_Objetos()
Ej.Ejecutar_Ejemplo()
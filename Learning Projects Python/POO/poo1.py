class Coche():
    ###Creacion de metodo constructor
    def __init__(self): #El constructor SIEMPRE se llama init
        self.largo=2500
        self.ancho=1000
        #propiedad encapsulada (privada).- dos guiones bajos
        self.__ruedas=4
        self.enMarcha=True
    ventanillas=6

    def arrancar(self,arrancamos):
        if arrancamos==True:
            print("ya esta arrancado")
        else:
            self.enMarcha=True
    

miCoche=Coche()
print("Ventanillas ", miCoche.ventanillas)
print(miCoche.enMarcha)
miCoche.arrancar(miCoche.enMarcha)
print(miCoche.enMarcha)
miCoche2=Coche()
print("Largo: ", miCoche2.largo)
#print("Ruedas: ", miCoche2.__ruedas) ERROR????
miCoche2.__ruedas=6
print("Ruedas: ", miCoche2.__ruedas)

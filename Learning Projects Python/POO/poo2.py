class Coche():
    ###Creacion de metodo constructor
    def __init__(self): #El constructor SIEMPRE se llama init
        self.largo=2500
        self.ancho=1000
        #propiedad encapsulada (privada).- dos guiones bajos
        self.__ruedas=4
        self.enMarcha=False
    ventanillas=6

    def arrancar(self,arrancamos):
        if arrancamos==True:
            print("ya esta arrancado")
        else:
            check=self.__chequeo_interno()
            if(check):
                print("No hay errores. Arrancando")
                self.enMarcha=True
            else:
                print("hay Errores")
    
    def __chequeo_interno(self):
        print("Chequeando")
        self.gasolina="ok"
        self.puertas="cerradas"

        if(self.gasolina=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False

miCoche=Coche()
miCoche.arrancar(miCoche.enMarcha)
print("Ventanillas ", miCoche.ventanillas)
print(miCoche.enMarcha)
#print(miCoche.__chequeo_interno()) desde aqui no es accesible el metodo. Es privado, por los quiones bajos
miCoche.arrancar(miCoche.enMarcha)
print(miCoche.enMarcha)


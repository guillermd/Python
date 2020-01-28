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


class Moto(Vehiculos): #la herencia se consigue poniendo entre parentesis la clase de la que hereda
    pass    

moto= Moto("Honda","CBR")
print(moto.marca)
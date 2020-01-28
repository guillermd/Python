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
    hCaballito=""

    def caballito(self):
        self.hCaballito="Voy levantando al rueda delantera" 

    def estado(self): #Este metodo SOBREESCRIBE SIEMPRE el de la clase base
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEnMarcha: ", self.enMarcha, 
                "\nAcelera: ", self.acelera, "\nFrena:", self.frena, "\nSalto de caballito? ", self.hCaballito)  

class V_Electrico():
    def __init__(self):
        self.autonomia=100
    def cargarEnergia(self):
            self.cargando=True

class Bici_electrica(V_Electrico, Vehiculos): #Herencia Multiple. Tiene preferencia el constructor d la primera clase en la herencia
    pass
#miBici=Bici_electrica("Orbea","biciMad")#Error. Debe crearse con el constructor de V_Electrico

class Bici_electrica2(Vehiculos,V_Electrico): #Herencia Multiple. Tiene preferencia el constructor d la primera clase en la herencia
    pass

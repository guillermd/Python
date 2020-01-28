class Coche():
    def desplazamiento(self):
        print("Me estoy moviendo en coche")

class Moto():
    def desplazamiento(self):
        print("Me estoy moviendo en moto")
    
class Camion():
    def desplazamiento(self):
        print("Me estoy moviendo en camion")

def DesplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo=Coche()
DesplazamientoVehiculo(miVehiculo)
miVehiculo=Moto()
DesplazamientoVehiculo(miVehiculo)
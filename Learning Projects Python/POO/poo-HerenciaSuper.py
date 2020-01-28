class Persona():
    def __init__(self, nombre, edad, residencia):
        self.nombre=nombre
        self.edad=edad
        self.residencia=residencia  
    
    def suma(self):
        return 6+4

    def Descripcion(self):
        print("Nombre:", self.nombre, " Edad: ", self.edad, " Residencia: ", self.residencia)

class Empleado(Persona):
    def __init__(self, salario, antiguedad):
        super().__init__("jose",65,"Burgos")#super().- llama al metodo del padre que pone a continuacion. En este caso __init__
        self.salario=salario
        self.antiguedad=antiguedad


    def suma(self):
        return super().suma()

persona1=Empleado(1500,14)

print(isinstance(persona1, Empleado))#Devuelve true si el primer parametro es del tipo del segundo parametro
print(persona1.suma()) #esto ejecuta el metodo suma del padre
persona1.Descripcion()
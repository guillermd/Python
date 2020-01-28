class Alumno():
    def __init__(self):#inicializar atributos pidiendoles al usuario
        self.nombre=input("nombre del alumno:" )
        self.nota=input("nota del alumno: ")

    def printDatos(self):
        print("El alumno ", self.nombre, " ha sacado un: ", self.nota)
    
    def verNota(self):
        res="suspendido"
        if(int(self.nota)>4):
            res="aprobado"
        
        print ("El alumno ", self.nombre, "ha sacado un ", self.nota, ". Entonces ha", res)

class Alumna():
    def __init__(self, nombre, nota):#inicializar atributos
        self.nombre=nombre
        self.nota=nota
    
    def printDatos(self):
        print("La alumna ", self.nombre, " ha sacado un: ", self.nota)
    
    def verNota(self):
        res="suspendido"
        if(int(self.nota)>4):
            res="aprobado"
        
        print ("La alumna ", self.nombre, "ha sacado un ", self.nota, ". Entonces ha", res)
Al1=Alumno()

Al1.verNota()



import pickle

#creamos el objeto a serializar
class Persona():
    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado una persona nueva, se llama ", self.nombre)
    
    #Este metodo convierte en cadena de texto la informacion de un objeto
    def __str__(self):
        return "{}{}{}".format(self.nombre, self.genero, self.edad)
    
class Ejemplo1():
    def PruebaMetodoSTR(self):
        p=Persona("Luis", "masculino",45)

#Ej=Ejemplo1()
#Ej.PruebaMetodoSTR()

class Lista_personas:    
    personas=[]   
    
    def __init__(self):
        listaDePersonas=open("listaExternaPersonas","ab+") #ab+ => Agregar informacion binaria
        listaDePersonas.seek(0)
        try:     
            self.personas=pickle.load(listaDePersonas)
            print("Se han cargado los datos de {} personas".format(len(self.personas)))
        except:
            print("el fichero esta vacio")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)
            
    def Agregar_personas(self, p):
        self.personas.append(p)
        self.Guardar_Personas_Fichero_Externo()

    def Muestra_personas(self):
        for p in self.personas:
            print(p)
    
    def Guardar_Personas_Fichero_Externo(self):
        Lista_personas=open("listaExternaPersonas", "wb")
        pickle.dump(self.personas, Lista_personas)
        Lista_personas.close()
        del(Lista_personas)

    def MostrarInfoPersonasFicheroExterno(self):
        print("Informacion del fichero externo")
        for c in self.personas:
            print(c)
    
    def BorrarPersona(self, nombre):
        ficheroLectura=open("listaExternaPersonas", "rb")        
        misPersonas=pickle.load(ficheroLectura)
        for p in misPersonas:
            if(p.nombre.strip()==nombre.strip()):
                misPersonas.remove(p)
        ficheroLectura.close()
        del(ficheroLectura)
        ficheroEscritura=open("listaExternaPersonas", "wb")        
        pickle.dump(misPersonas, ficheroEscritura)  


miLista=Lista_personas()
#p=Persona("XXX ", "YYYY ",15)
#miLista.Agregar_personas(p)
#p=Persona("JJJ ", "sdfsd ",55)
#miLista.Agregar_personas(p)
#miLista.BorrarPersona("ANA")
miLista.MostrarInfoPersonasFicheroExterno()


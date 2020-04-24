'''
Escriba una funcion es_bisiesto() 
que determine si un año determinado 
es un año bisiesto.Un año bisiesto 
es divisible por 4, pero no por 100.
===================================================
def es_bisiesto(anyo):
    if(anyo%4==0 and anyo%4!=100):
        return("El año es bisiesto")
    return("El año no es bisiesto")

print(es_bisiesto(int(input("Introduzca un año:"))))
===================================================
'''
'''
Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla.
===================================================

class Persona():
    def __init__(self, nombre, anyo):
        self.nombre=nombre
        self.anyo=anyo

anyoActual=int(input('Introduce el año actual:'))
lista=[]
count=0
for item in range(5):
    count+=1
    n=input('Introduce el nombre:')
    e=input('Introduce su año de nacimiento:')
    p=Persona(n, int(e))    
    lista.append(p)

for i in lista:
    print ("La edad de" , i.nombre, "es " ,anyoActual-i.anyo)
print("items", len(lista))
==========================================================
'''
#Ejercicio 1
#Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.


#Ejercicio 2
#Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.


#Ejercicio 3
#Escribir una función que reciba un número entero positivo y devuelva su factorial.


#Ejercicio 4
#Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.


#Ejercicio 5
#Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.


#Ejercicio 6
#Escribir una función que reciba una muestra de números en una lista y devuelva su media.


#Ejercicio 7
#Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.


#Ejercicio 8
#Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.


#Ejercicio 9
#Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.


#Ejercicio 10
#Escribir una que convierta un número decimal en binario y otra que convierta un número binario en decimal.


#Ejercicio 11
#Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.
#6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
#fname = input("Enter file name: ")
#if len(fname) < 1 : fname = "r.txt"
#count=0
#fh = open(fname)
#for line in fh: 
#    l=line.split()
#    print("len: ",len(l))
#    print("len: ",len(1))
#    if(len(l)>1):
#        t=l[0]
#        if (t == "From"):
#    		print(l[1])
#    		count = count+1 

#print("There were", count, "lines in the file with From as the first word")
name = "r.txt"
dicc= dict() #counts
lista=[] #names
if len(name) < 1 : name = "r.txt"
handle = open(name)
for line in handle:
    l=line.split()    
    if len(l)>1 :        
        t=l[0]
        if (t == "From"):
            lista.append(l[5].split(":")[0])#corresponde con la hora del correo  

for l in lista:
    dicc[l]=dicc.get(l,0)+1

for k,v in sorted(dicc.items()):
    print (k,v)

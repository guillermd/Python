#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
class Ejercicio2():
    def EjecutarEjercicio(self):
        try:
            edad=input(print("Dime tu edad:"))        
            for i in range(int(edad)):
                print("Años: ", i)
        except ValueError:
            print("Mete un puto numero")

#Ejercicio 3
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los 
# números impares desde 1 hasta ese número separados por comas.
class Ejercicio3():
    def EjecutarEjercicio(self):
        num=int(input(print("Dame un numero: ")))
        cadena= ""
        for i in range(1,num+1):
            cadena+= str(i) + ", "
        caracteres=len(cadena)
        cadena=cadena[:int(caracteres-2)]
        print (cadena)

#Ejercicio 4
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde 
# ese número hasta cero separados por comas.
class Ejercicio4():
    def EjecutarEjercicio(self):
        num=int(input(print("Dame un numero: ")))
        cadena= ""
        for i in range(num, 0, -1):
            cadena+= str(i) + ", "
        cadena+="0"
        print (cadena)

#Ejercicio 5
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
# y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
class Ejercicio5():
    def EjecutarEjercicio(self):
        cantidad=int(input(print("Cantidad a invertir:" )))
        interes=float(input(print("Interes anual:" )))
        anyos=int(input(print("Años de la inversion:" )))
        for i in range(1,anyos):
            print("Año ", i)
            intTotal=cantidad*(interes*0.01)
            total=round(cantidad+intTotal,2)
            print(total)
            cantidad=total

#Ejercicio 6
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo,
#de altura el número introducido.

#*
#**
#***
#****
#*****
class Ejercicio6:
    def EjecutarEjercicio(self):
        altura=input(print("dime q altura quieres:"))
        cadena=""
        for i in range(int(altura)):
            cadena=""
            for a in range(i):
                cadena+="*"
            print(cadena)
 

#Ejercicio 7
#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
class Ejercicio7():
    def EjecutarEjercicio(self):
        for i in range(1,11):
            for a in range(1,11):
                print(i, "*", a,"=", i*a)

#Ejercicio 8
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

#1
#3 1
#5 3 1
#7 5 3 1
#9 7 5 3 1
class Ejercicio8():
    def EjecutarEjercicio(self):
        try:    
            num=input(print("Dame un numero:"))
            lista=[]
            for i in range(1, int(num),2):
                lista.insert(0,i)                
                print(lista)
            
        except ValueError:
            print("Mete un puto numero")
#Ejercicio 9
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
class Ejercicio9():
    def EjecutarEjercicio(self):
        password="contraseña"
        contraseña="."
        while contraseña != password:
            contraseña=input(print("mete contraseña:"))
       
        print("contraseña aceptada")
#Ejercicio 10
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
class Ejercicio10():
    def EjecutarEjercicio(self):
        num=int(input(print("Mete un numero:")))
        cont=0
        for i in range(1,num):
            if num%i==0:
                cont+=1        
        if(cont<=2):
            print("El numero es primo - ", cont)
        else:
            print("El numero no es primo - ", cont)


Ej=Ejercicio5()
Ej.EjecutarEjercicio()
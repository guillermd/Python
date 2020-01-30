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


#Ejercicio 4
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde 
# ese número hasta cero separados por comas.


#Ejercicio 5
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
# y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.


#Ejercicio 6
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo,
#de altura el número introducido.

#*
#**
#***
#****
#*****


#Ejercicio 7
#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.


#Ejercicio 8
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

#1
#3 1
#5 3 1
#7 5 3 1
#9 7 5 3 1

#Ejercicio 9
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.


#Ejercicio 10
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

Ej=Ejercicio2()
Ej.EjecutarEjercicio()
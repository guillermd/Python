#Ejercicio 1
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
class Ejercicio1():
    def EjecutarEjercicio(self):
        edad=int(input(print("Dame tu edad:")))
        if(edad<18):
            print("eres menor")
        else:
            print("eres mayor de edad")

#Ejercicio 2
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada 
# en la variable sin tener en cuenta mayúsculas y minúsculas.
class Ejercicio2():
    def EjecutarEjercicio(self):
        appPassword="contraSeÑA"
        userPassword=(input(print("pon la contraseña:")).upper())
        if(appPassword.upper()==userPassword):
            print("contraseña correcta")
        else:
            print("contraseña incorrecta")

#Ejercicio 3
#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
class Ejercicio3():
    def EjecutarEjercicio(self):
        numA=float(input(print("dame un numero:")))
        numB=float(input(print("dame otro numero:")))
        try:
            print(numA/numB)
        except ZeroDivisionError:
            print("ERROR!!!! No se puede dividir entre cero")

#Ejercicio 4
#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. 
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
class Ejercicio4():
    def EjecutarEjercicio(self):
        edad=int(input(print("dime tu edad:")))
        ingresos=int(input(print("dime tu edad:")))
        if(edad > 16 and ingresos>1000):
            print("Debes pagar impuestos")
        else:
            print("No debes pagar impuestos")

#Ejercicio 5
#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
# El grupo A esta formado por las mujeres con un nombre anterior a la M y 
# los hombres con un nombre posterior a la N y el grupo B por el resto. 
# Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.


#Ejercicio 6
#Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
#Renta	Tipo impositivo
#Menos de 10000€	5%
#Entre 10000€ y 20000€	15%
#Entre 200000€ y 35000€	20%
#Entre 350000€ y 60000€	30%
#Más de 60000€	45%
#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
class Ejercicio6():
    def EjecutarEjercicio(self):
        renta=int(input(print("dime tu renta anual:")))
        if(renta<10000):
            print("Debes pagar el 5%")
        elif(renta<20000):
            print("Debes pagar el 15%")
        elif(renta<35000):
            print("Debes pagar el 20%")
        elif(renta<60000):
            print("Debes pagar el 30%")
        elif(renta>60000):
            print("Debes pagar el 45%")

#Ejercicio 7
#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, 
# y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
class Ejercicio7():
    def EjecutarEjercicio(self):
        peso=int(input(print("dime tu peso:")))
        estatura=float(input(print("dime tu estatura(metros):")))       
        imc=self.calculaIMC(peso, estatura) 
        print("Tu índice de masa corporal es", imc)

    def calculaIMC(self, peso, estatura):
        return round(peso/(estatura**2),2)

#Ejercicio 8
#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> 
# y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente 
# y el resto de la división entera respectivamente.
class Ejercicio8():
    def EjecutarEjercicio(self):
        num1=int(input(print("numero 1:")))
        num2=int(input(print("numero 2:")))     
        print("la división de ",num1," entre ", num2 ,"da un cociente ",int(num1//num2) ," y un resto", int(num1%num2))


Ej=Ejercicio8()
Ej.EjecutarEjercicio()
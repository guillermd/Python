'''
try:
    num1=int(input("primer numero: "))
    num2=int(input("segundo numero: "))
except ValueError:
        print("Mete un puto numero")
except NameError:
        print("Name Error")
finally:
    print("Ejecucion terminada")
def Divide(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("no dividas por zero capullo")    
print(Divide(num1, num2))
'''
#Raise Error
import math

def calculaRaiz(num1):
    if num1<0:
        raise ValueError("no puedes poner numeros negativos")        
    else:
        return math.sqrt(num1)
    
op1=(int(input("Introduce un numero:")))

try:
    print(calculaRaiz(op1))
except ValueError as ErrorNumeroNegativo:
    print(ErrorNumeroNegativo)    

print ("Programa terminado")

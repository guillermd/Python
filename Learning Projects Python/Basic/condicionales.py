#OPERADORES: > < == >= <= !=
def evaluacion (nota):
    valor="aprobado"
    if nota<5:
        valor="suspenso"  
    #elif: => else if  
    #else:
        #####LO QUE SEA
    return valor
print(evaluacion(4))
#introducir valores por teclado
#cualquier dato introducido por teclado es un texto. para transformar a entero => funcion int()

tuNota=input("Dame tu nota: ")
#print(evaluacion(tuNota))#error
print(evaluacion(int(tuNota)))
#if CONCATENADOS
#if 0<edad<100:.- compara 0 con edad y si se cumple compara edad con 100
#OPERADOR IN.- if variable in ("item1", "item2", "item3"):
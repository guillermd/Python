#Funcion Filter
#Verifica que los elementos de una secuencia cumplen una condicion, devolviendo un iterador con los elementos q cumplen dicha condicion

def numeros_pares(num):
    if(num % 2==0):
        return True

numeros=[5,32,8,42,81,66,92]
print(list(filter(numeros_pares, numeros)))

#usando lambda
print(list(filter(lambda num_par:num_par % 2==0, numeros)))

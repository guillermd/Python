#esto seria una funcion normal
def generaPares(limite):
    num=1
    miLista=[]
    while num<limite:
        miLista.append(num*2)
        num=num+1
    return miLista

print (generaPares(10))

#con generador
def generaParesGenerador(limite):
    num=1
    
    while num<limite:
        yield num*2
        num=num+1
 #devuelvePares es el objeto generador
devuelvePares=generaParesGenerador(10)
#entre llamada y llamada el metodo generador se queda en pausa
print(next(devuelvePares))
print("codigo entre medias")
print(next(devuelvePares))
print("mas codigo")
print(next(devuelvePares))
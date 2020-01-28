miTupla=("item1", 18, "item3")
print(miTupla)
#busqueda de elementos
print(miTupla.index("item3"))
#Convertir una tuppla en Lista
miLista=list(miTupla)
print (miLista)
#Convertir una lista en tupla
miLista.append(7)
miTupla2=tuple(miLista)
print (miTupla2)
#buscar elementos en la tupla => in
print("item1" in miTupla)
#contar las veces que esta un elemento en la tupla
print(miTupla.count(18))
#longitud de una tupla
print(len(miTupla2))
#asignar cada item de la tupla a una variable distitna. Asigna por orden cada valor a la variable 
miTupla3=("pepe", 13,3,2010)
nombre, dia, mes, anyo = miTupla3
print(nombre); print(dia);print(mes);print(anyo)
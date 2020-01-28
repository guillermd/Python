miLista=["item2", "item3"]
miTupla=(1,2,3,4)
#Almacenan cualquier tipo de dato
miDiccionario={"España":"Madrid", "Francia":"Paris"}
print(miDiccionario)
print(miDiccionario["España"])
#Agregar valores
miDiccionario["Italia"]="Roma"
#Eliminar valores
del miDiccionario["Francia"]

miDiccionario2={miTupla[0]:"numero 1", miTupla[1]:"numero2"}
print(miDiccionario2)

miDiccionario3={23:"Jordan", "nombre":"Michael", "anillos":[1991,1992]}
print(miDiccionario3)

#metodos importantes
print(miDiccionario2.keys())
print(miDiccionario2.values())
print(len(miDiccionario2))
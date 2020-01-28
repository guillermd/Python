
ListaDeLetras=["A","B", "C", "D", "E","F","G", "H", "I", "J", "K", "L", "M", "N", "O", "P","Q", "R","S"]

print("ListaDeLetras: ")
print (ListaDeLetras)
print("ListaDeLetras[0:3]:Muestra desde el indice 0 hasta el anterior al 3 ")
print(ListaDeLetras[0:3])
print("ListaDeLetras.index(item):Muestra el indice del valor pasado. Si hay mas de un valor igual, devolverá el primero que se encuentre ")
print(ListaDeLetras.index("E"))
print("ListaDeLetras[-2]:Muestra desde el penultimo item. Cuenta desde atras...NO empieza a contar en 0 ")
print(ListaDeLetras[-2])
print("ListaDeLetras[3:]:Muestra desde el el indice 3 hasta el final"); print(ListaDeLetras[3:])
print("ListaDeLetras[:4]:Muestra desde el indice 0 hasta el anterior al 4"); print(ListaDeLetras[:4])
print("ListaDeLetras[2:6]:Muestra desde el indice 2 hasta el anterior al 6 "); print(ListaDeLetras[2:6])
print("ListaDeLetras[2:6]:Muestra desde el indice 3 hasta el anterior al 18, saltando dos "); print(ListaDeLetras[3:18:2])
print("ListaDeLetras[2:6]:Muestra desde el indice 3 hasta el anterior al 18, saltando tres "); print(ListaDeLetras[3:18:3])
print("Añade elementos a la lista ListaDeLetras.append(""Z"")"); ListaDeLetras.append("Z"); print (ListaDeLetras)
print("Borrar elementos de la lista ListaDeLetras.remove(""Z"")"); ListaDeLetras.remove("Z"); print (ListaDeLetras)
print("Inserta elementos a la lista ListaDeLetras.insert(3,""Z"")"); ListaDeLetras.insert(3,"Z"); print (ListaDeLetras)
print("Añade varios elementos a la lista ListaDeLetras.extend([item1, item2...]])"); ListaDeLetras.extend(["item1, item2, item3"])
print (ListaDeLetras)
print("ListaDeLetras.pop():Borra ultimo elemento"); print(ListaDeLetras.pop())
print("ListaDeLetras.remove(item):Borra el elemento seleccionado "); ListaDeLetras.remove("B")
print (ListaDeLetras)
print("G" in ListaDeLetras) #Devolvera true si G existe en la lista
ListaDeNUmeros=[1,2,3,4,5,6]
ListaTotal=ListaDeNUmeros+ListaDeLetras#El poerador + sirve para concatenar listas
print(ListaTotal)
ListaDeNUmeros2=[7,8,9]*2
print(ListaDeNUmeros2)

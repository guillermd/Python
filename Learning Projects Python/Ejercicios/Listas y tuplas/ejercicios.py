#Ejercicio 1
#Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
class ejercicio1():
    def HacerEjercicio(self):   
        asigns=[]     
        while(len(asigns)<4):
            a=input(print("Introduce un asignatura:"))
            asigns.append(a)
        print("las asignaturas introducidos son", asigns)


#Ejercicio 3
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, 
# y después las muestre por pantalla con el mensaje 
# En <asignatura> has sacado <nota> 
# donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las 
# correspondientes notas introducidas por el usuario.
class ejercicio3():
    pass
#Ejercicio 4
#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
class ejercicio4():    
    def HacerEjercicio(self):   
        lista=[]     
        while(len(lista)<8):
            num=int(input(print("Introduce un numero:")))
            lista.append(num)
        lista.sort()
        print("los numeros introducidos son", lista)


#Ejercicio 5
#Escribir un programa que almacene en una lista los números del 1 al 10 y 
# los muestre por pantalla en orden inverso separados por comas.
class ejercicio5():
    def HacerEjercicio(self):
        lista=[0,1,2,3,4,5,6,7,8,9,10]
        cadena=""
        for i in lista:
            cadena+=str(i)+ ", "
        print (cadena)
    

#Ejercicio 6
#Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
# pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. 
# Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
class ejercicio6():
    def HacerEjercicio(self):
        lista=['matematicas','lengua','ingles','chino']
        listatemp=lista.copy()
        for i in listatemp:
            nota=int(input(print("Que has sacado en ", i)))
            if(nota>4):
                lista.remove(i)
        print("tienes que repetir ", lista)
#Ejercicio 7
#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, 
# y muestre por pantalla la lista resultante.
class ejercicio7():
    def HacerEjercicio(self):
        ListaDeLetras=["A","B", "C", "D", "E","F","G", "H", "I", "J", "K", "L", "M", "N", "O", "P","Q", "R","S", "T", "U", "V", "W", "X", "Y", "Z"]
        listaABorrar=[]
        for i in ListaDeLetras[2::3]:
            listaABorrar.append(i)
        for a in listaABorrar:
            ListaDeLetras.remove(a)
        print("lista de borradas: ", listaABorrar)
        print("---")
        print("lista resultante: ",ListaDeLetras)

#Ejercicio 8
#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
class ejercicio8():
    def HacerEjercicio(self):
        cad=input(print("introduzca la palabra a analizar"))
        cadCopy=""
        for i in range(1,len(cad)+1): 
            cadCopy+=cad[len(cad)-i]
        if(cad.upper()==cadCopy.upper()):
            print("palindromo")
        else:
            print("no palindromo")

#Ejercicio 9
#Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
class ejercicio9():
    def HacerEjercicio(self):
        aes=0; ees=0; ies=0; oes=0; ues=0
        palabra=input("Introduce una palabra:")
        for i in palabra.lower():
            if(i=="a"):
                aes+=1
            elif(i=="e"):
                ees+=1
            elif(i=="i"):
                ies+=1
            elif(i=="o"):
                oes+=1
            elif(i=="u"):
                ues+=1

        print("numero de a:",aes,"numero de e:",ees,"numero de i:",ies,"numero de o:",oes,"numero de u:",ues)

#Ejercicio 10
#Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla 
# el menor y el mayor de los precios.
class ejercicio10():
    pass

#Ejercicio 11
#Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.
class ejercicio11():
    pass

#Ejercicio 12
#Escribir un programa que almacene las matrices 𝐴=(142536)𝑦𝐵=⎛⎝⎜⎜⎜⎜⎜−101011⎞⎠⎟⎟⎟⎟⎟
#en una lista y muestre por pantalla su producto.
#Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.
class ejercicio12():
    pass

#Ejercicio 13
#Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.
class ejercicio13():
    pass

ej = ejercicio7()
ej.HacerEjercicio()
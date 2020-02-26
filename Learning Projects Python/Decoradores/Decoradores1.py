#Los decoradores son funciones que agregan funcionalidad a otras funciones
#ESTRUCTURA
#3 funciones (A, B y C) donde A recibe como parametro a B para devolver a C
#Un decorador devuelve una funcion
#def funcionA(funcionB):
#   funcioninterna():
#   return funcionC
def funcion_decoradora(funcion_parametro): #Funcion A
    def funcion_interior(*args): #*args.- indica que recibira un numero indeterminado de parametros, desde 0 hasta infinito
        print("antes")
        funcion_parametro(*args)
        print("despues")
    return funcion_interior

def funcion_decoradora_ClaveValor(funcion_parametro): #Funcion A
    def funcion_interior(*args, **kwargs): #*args.- indica que recibira un numero indeterminado de parametros, desde 0 hasta infinito. **kwargs argumentos con clave
        print("antes de potencia")
        funcion_parametro(*args, **kwargs)
        print("despues de potencia")
    return funcion_interior

@funcion_decoradora #llamada al decorador
def suma(num1, num2):    
    print(num1+num2)

@funcion_decoradora #llamada al decorador
def resta():
    print(30-10)

@funcion_decoradora_ClaveValor
def potencia(base, exponente):
    print(pow(base, exponente))

suma(7,3)
resta()
potencia(base=5, exponente=3)
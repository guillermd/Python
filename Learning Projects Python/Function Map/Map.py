#La funcion Map aplica una funcion a cada elemento de una lista iterable devolviendo una lita con los resultados
class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario

    def __str__(self):
        return "{} trabaja como {} y cobra {} €".format(self.nombre, self.cargo, self.salario)

empleadosLista=[
    Empleado("juan", "director", 1500),
    Empleado("Alicia", "gerente", 3500),
    Empleado("Antonio", "vendedor", 2100),
    Empleado("juana", "atencion", 1800),
]

def calculo_comision(empleado):
    empleado.salario=empleado.salario*1.03
    return empleado

lista_empleados_comision=map(calculo_comision,empleadosLista) #param1:funcion, param2:lista
for e in lista_empleados_comision:    
    print(e)

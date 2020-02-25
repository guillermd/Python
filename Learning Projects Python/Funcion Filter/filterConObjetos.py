class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario

    def __str__(self):
        return "{} trabaja como {} y cobra {} €".format(self.nombre, self.cargo, self.salario)

empleadosLista=[
    Empleado("juan", "director", 75000),
    Empleado("Alicia", "gerente", 55000),
    Empleado("Antonio", "vendedor", 45000),
    Empleado("juana", "atencion", 35000),
]

#obtener lista de empleados que ganen mas de 50000
salarios_altos=filter(lambda empleado:empleado.salario>50000, empleadosLista)
for e in salarios_altos:
    #print("{} trabaja como {} y cobra {} €".format(e.nombre, e.cargo, e.salario)) la funcion __str__ tiene el texto por defecto al hacer print()
    print(e)
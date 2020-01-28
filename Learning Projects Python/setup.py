#contiene una descripcion del paquete a distribuir
from setuptools import setup
setup(  
    name="paqueteCalculos", 
    version="1.0",
    description="Paquete de calculos básicos",
    author="yo",
    author_email="guillermd@gmail.com",
    url="www.XXXX.es",
    packages=["Paquetes","Paquetes"], #si hubiera mas carpetas por medio, seria ["carpeta","carpeta.subcarpeta.."]
)

#Para hacer el paquete distribuible habria que poner en cmd, desde la carpeta raiz de la aplicacion => python setup.py sdist
#En este caso seria => c:\users\ggarcima\documents\learning Projects Python> python setup.py sdist
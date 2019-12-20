#9. Funcion que valida si un numero es capicua
import os
from Rojas.library import *

numbr=os.sys.argv[1]

nine=es_capicua(numbr)
if nine==True:
    print(numbr," es un numero capicua")
if (nine=="Invalido"):
    print(numbr," no es un numero")
else:
    print(numbr," no es capicua")

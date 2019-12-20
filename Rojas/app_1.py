# Programa que utiliza la funcion que valida un numero de dni
#importamos la libreria
import os
from Rojas.library import *

dni=int(os.sys.argv[1])
one= es_dni(dni)

#
if one==True:
   print(dni," Es un numero de dni")
else:
    print(dni," No es un numero dni")



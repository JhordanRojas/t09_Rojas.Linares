# Programa que utiliza la funcion que valida un numero de dni
#importamos la libreria
import os
import library

dni=os.sys.argv[1]
one=library.es_dni(dni)

#
if one==True:
   print(dni," Es un numero de dni")
else:
    print(dni," No es un numero dni")



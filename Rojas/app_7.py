#7. Funcion que pide un nombre
import os
import library

nombre=os.sys.argv[1]

seve=library.valid_nombre(nombre)
if seve==True:
    print("El nombre es ", seve)
else:
    print(seve," no es un nombre")




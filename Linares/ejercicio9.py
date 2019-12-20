import os
import libreria

a=int(os.sys.argv[1])
b=int(os.sys.argv[2])

fuerza=libreria.fuerza_electrostatica(a,b)
print("La fuerza electrostatica es:", fuerza)

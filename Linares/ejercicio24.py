import os
import libreria

r=int(os.sys.argv[1])
s=int(os.sys.argv[2])

fuerza=libreria.fuerza_de_rozamiento(r,s)
print("La fuerza de rozamiento:", fuerza)

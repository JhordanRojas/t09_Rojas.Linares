import os
import libreria

a=int(os.sys.argv[1])
b=int(os.sys.argv[2])

velocidad=libreria.velocidad_tangencial(a,b)
print("La velocidad tangencial es:", velocidad)

import os
import libreria

m=int(os.sys.argv[1])
n=int(os.sys.argv[2])

temperatura=libreria.pedir_temperatura_corporal(m,n)
print("La temperatura es:", temperatura)

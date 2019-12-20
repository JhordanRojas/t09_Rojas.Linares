import os
import libreria

x=int(os.sys.argv[1])
y=int(os.sys.argv[2])
z=int(os.sys.argv[3])

zona=libreria.zona_esferica(x,y,z)
print("La zona esferica es:", zona)

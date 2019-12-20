import os
import libreria

z=int(os.sys.argv[1])
x=int(os.sys.argv[2])
y=int(os.sys.argv[3])

dilatacion=libreria.dilatacion_superficial(z,x,y)
print("La dilatacion superficial es:", dilatacion)

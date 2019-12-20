import os
import libreria

a=int(os.sys.argv[1])
b=int(os.sys.argv[2])

variacion=libreria.variacion_de_energia_interna(a,b)
print("La variacion de energia interna es:", variacion)

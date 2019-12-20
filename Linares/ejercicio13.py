import os
import libreria

q=int(os.sys.argv[1])
w=int(os.sys.argv[2])

aceleracion_angular1=libreria.aceleracion_angular(q,w)
print("La aceleracion angular es:", aceleracion_angular1)

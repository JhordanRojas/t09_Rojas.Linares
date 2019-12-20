import os
import libreria

a=int(os.sys.argv[1])
b=int(os.sys.argv[2])
c=int(os.sys.argv[3])

empuje=libreria.empuje_de_un_liquido(a,b,c)
print("El empuje es:", empuje)

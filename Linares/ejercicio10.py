import os
import libreria

l=int(os.sys.argv[1])
m=int(os.sys.argv[2])

dif_de_pot=libreria.diferencia_de_potencial(l,m)
print("La diferencia de potencial es:", dif_de_pot)

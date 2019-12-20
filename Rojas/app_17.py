#17. Funcion que calcula el tiempo de encuentro entre dos moviles
import os
import library

vel_1=os.sys.argv[1]
vel_2=os.sys.argv[2]
distancia=os.sys.argv[3]

t_encuetro=library.tiempo_encuentro(vel_1,vel_2,distancia)
print("el tiempo de encuentro de los moviles es:",t_encuetro)

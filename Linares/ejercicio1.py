import libreria
import os

a=int(os.sys.argv[1])
b=int(os.sys.argv[2])
c=int(os.sys.argv[3])
presion_hidrostatica=libreria.presion_hidrostatica(a,b,c)

print("la presion hidrostatica es:", presion_hidrostatica)


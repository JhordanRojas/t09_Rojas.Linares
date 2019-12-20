import os
import libreria

a=int(os.sys.argv[1])
b=int(os.sys.argv[2])

nota1=libreria.pedir_notas_de_fin_de_ciclo(b)
nota2=libreria.pedir_notas_de_fin_de_ciclo(a)
prom=libreria.promedio(nota1, nota2)
print("El promedio de notas es:", prom)

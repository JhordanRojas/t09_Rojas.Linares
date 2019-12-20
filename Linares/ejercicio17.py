import os
import libreria

n=int(os.sys.argv[1])
z=int(os.sys.argv[2])
p=int(os.sys.argv[3])

energia_potencial_g=libreria.energia_pot_grav(n,z,p)
print("La energia potencial gravitatoria es:", energia_potencial_g)

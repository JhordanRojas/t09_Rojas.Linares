#3. Funcion que Valida un codigo universitario
import os
from Rojas.library import *

codi=os.sys.argv[1]
thre=codigo_uni(codi)
if thre == True:
    print(codi," es un codigo valido")
else:
    print(codi," no es un codigo valido")

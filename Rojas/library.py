#auxiliares
def validar_entero(msg):
    if(msg.isdigit() == True):
        return True
    else:
        return False
#fin_def

def pedir_rango(msg, r1, r2):
    rango_invalido=True
    valor=0
    while(rango_invalido):
        valor=(msg)
        rango_invalido=(valor < r1 or valor > r2)
    #fin_while
    return valor
#fin_def


#1. Funcion que valida el numero de un dni
def es_dni (num):
    digito=num.isdigit()
    if (digito == True):
       if (len(num)== 8):
           return True
       else:
           return False
    else:
        return False
#Fin_def

#2. Funcion que valida el numero de un celular
def pedir_cel(msj):
    invalido=True
    numero=0
    while invalido:
        numero=(msj)
        longi=(len(numero)==9)
        invalido=(numero.isdigit()== False and longi==True)
    #fin_while
    return int(numero)
#Fin_def

#3. Funcion que Valida un codigo universitario
def codigo_uni(msg):
 codigo=(msg)
 long=len(codigo)
 num=codigo[0:5]
 gui=codigo[6:7]
 letra=codigo[7:8]
 if long == 8:
   if (num.isdigit() == True and
       gui == "-" and
       letra.isalpha() == True):
       return True
   else:
       if letra.isalpha()==False:
           return False
 else:
     return "Invalido"
#Fin_def

#4. Funcion que calcula el area de un circulo
def area_circulo(radio):
    area=3.1416*int(radio)**2
    return area
#Fin_def

#5. Funcion que calcula el area de un trapecio
def area_trapecio(b1,b2,h):
    area_trap=(int(b1)+int(b2))*(int(h)/2)
    return area_trap
#Fin_def

#6. Funcion que pide la edadde una persona mayor de edad
def es_mayor_edad(men):
    if validar_entero(men)==True:
        mayor=True
        if(mayor ):
           mayor=(int(men)>18 or int(men)<110)
           return True
        else:
           return False
    else:
        return "Invalido"

#Fin_def

#7. Funcion que pide un nombre
def valid_nombre(mssg):
    no_name=True
    if(no_name):
        valor=(mssg)
        no_name=(valor.isalpha()==False and len(valor)<3)
        return False
    else:
        return True
#Fin_def


#8. Funcion que valida si un numero es multiplo de 5
def multiplo_de_5(numero):
    multi_5=(int(numero)%5 ==0)
    if multi_5==True:
        return True
    else:
        return False

#9. Funcion que valida si un numero es capicua
def es_capicua (num):
    invalid=(num.isdigit()==False)
    if invalid==False:
        if num == num[::-1]:
             return True
        else:
             return False
    else:
        return "Invalido"
#Fin_def

#10.Funcion que valida el año de nacimiento de un mayor de edad
def cump_mayor_edad(men):
    if validar_entero(men)==True:
        mayor=True
        if(mayor ):
           mayor=(int(men)>1919 or int(men)<2001)
           return True
        else:
           return False
    else:
        return "Invalido"
#Fin_def


#11. Funcion que calcula el volumen de un cubo
def vol_cube(lado):
    vol=int(lado)**3
    return vol
#Fin_def
#12. Funcion que calcula la densidad de un cuerpo
def densidad(masa,vol):
    densd=int(masa)/int(vol)
    return densd
#Fin_def

#13.Funcion que calcula el area de un rectangulo
def area_rectangulo(ancho,alto):
    areaa=int(ancho)*int(alto)
    return areaa
#Fin_def

#14. Funcion que calcula la sumatoria de numeros naturales
def sumatoria_nat(n_sumandos):
    sumatoria=(int(n_sumandos)**2)+(int(n_sumandos)/2)
    return int(sumatoria)
#Fin_def

#15. Funcion que calcula el porcentaje
def porcentaje(parte,todo):
    percent=(int(parte)/int(todo))*100
    return percent
#Fin_def

#16.funcion que calcula el area de una elipse
def area_elipse(r1,r2):
    pi=3.1415
    area_e=pi*(int(r1)+int(r2))
    return area_e
#Fin_def

#17. Funcion que calcula el tiempo de encuentro entre dos moviles
def tiempo_encuentro(v1,v2,distancia):
    t_en=(int(v1)+int(v2))/int(distancia)
    return t_en
#Fin_def

#18. Funcion que valida la temperatura
def temperatura(men):
    if validar_entero(men)==True:
        mayor=True
        if(mayor ):
           mayor=(int(men)>45 or int(men)<0)
           return True
        else:
           return False
    else:
        return "Invalido"

#Fin_def

#19. Funcion multiplicar 3 numeros
def mult_3(a1,a2,a3):
    mult=int(a1)*int(a2)*int(a3)
    return mult
#Fin_def

#20. Funcion que calcula el promedio de tres numeros
def promedio(c1,c2,c3):
    a=int(c1)
    b=int(c2)
    c=int(c3)
    prom=(a+b+c)/3
    return prom
#Fin_def

#21. Funcion que calcula el area lateral de un prisma reatangular
def area_lat_prism(ancho,largo,altura):
    area_lat=2*(int(ancho)+int(largo))*int(altura)
    return area_lat
#Fin_def

#22. Funcion que elige el numero mayor de dos
def mayor(a,b):
    if (a > b):
        return a
    else:
        return b
#Fin_def

#23. Funcion que calcula una potenciacion
def potencacion(base,exponente):
    potencia=int(base)**int(exponente)
    return potencia
#Fin_def

#24. Funcion que la fuerza de un cuerpo
def fuerza(masa,aceleracion):
    force=int(masa)*int(aceleracion)
    return force
#Fin_def

#25. Funcion que calcula la suma de los n primeros cuadrados perfectos
def sum_cuadrados(n):
    a=int(n)
    sumatt=(a/6)*(a+1)*(a+a+1)
    return int(sumatt)
#Fin_def






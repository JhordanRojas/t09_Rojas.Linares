#auxiliares
def pedir_entero(msg):
    entero_invalido=True
    valor=0
    while(entero_invalido):
        valor=input(msg)
        entero_invalido=( valor.isdigit() == False )
    #fin_while
    return int(valor)
#fin_def

def pedir_rango(msg, r1, r2):
    rango_invalido=True
    valor=0
    while(rango_invalido):
        valor=pedir_entero(msg)
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
        numero=input(msj)
        longi=(len(numero)==9)
        invalido=(numero.isdigit()== False and longi==True)
    #fin_while
    return int(numero)
#Fin_def

#3. Funcion que Valida un codigo universitario

def codigo_uni(msg):
 codigo=input(msg)
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
    area=3.1416*radio**2
    return area
#Fin_def

#5. Funcion que calcula el area de un trapecio
def area_trapecio(b1,b2,h):
    area_trap=(b1+b2)*h/2
    return area_trap
#Fin_def

#6. Funcion que pide la edadde una persona mayor de edad
def pedir_mayor_edad(men):
    pedir_rango(men,18,110)
#Fin_def

#7. Funcion que pide un nombre
def pedir_nombre(mssg):
    no_name=True
    while (no_name):
        valor=input(mssg)
        no_name=(valor.isalpha()==False and len(valor)<3)
    return valor
#Fin_def


#8. Funcion que valida si un numero es multiplo de 5
def multiplo_de_5(numero):
    multi_5=(numero%5 == 0)
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
def pedir_anio_mayor(msj):
    pedir_rango(msj,1919,2001)
#Fin_def


#11. Funcion que calcula el volumen de un cubo
def vol_cube(lado):
    vol=lado**3
    return vol
#Fin_def
#12. Funcion que calcula la densidad de un cuerpo
def densidad(masa,vol):
    densd=masa/vol
    return densd
#Fin_def

#13.Funcion que calcula el area de un rectangulo
def area_rectangulo(ancho,alto):
    areaa=ancho*alto
    return areaa
#Fin_def

#14. Funcion que calcula la sumatoria de numeros naturales
def sumatoria_nat(n_sumandos):
    sumatoria=(n_sumandos**2+n_sumandos)/2
    return int(sumatoria)
#Fin_def

#15. Funcion que calcula el porcentaje
def porcentaje(parte,todo):
    percent=(parte/todo)*100
    return percent
#Fin_def

#16.funcion que calcula el area de una elipse
def area_elipse(r1,r2):
    pi=3.1415
    area_e=pi*(r1+r2)
    return area_e
#Fin_def

#17. Funcion que calcula el tiempo de encuentro entre dos moviles
def tiempo_encuentro(v1,v2,distancia):
    t_en=(v1+v2)/distancia
    return t_en
#Fin_def

#18. Funcion que valida la temperatura
def temperatura(msg):
    pedir_rango(msg,0,45)
#Fin_def

#19. Funcion multiplicar 3 numeros
def mult_3(a1,a2,a3):
    mult=a1*a2*a3
    return mult
#Fin_def

#20. Funcion que calcula el promedio de tres numeros
def promedio(c1,c2,c3):
    prom=(c1+c2+c3)/3
    return prom
#Fin_def

#21. Funcion que calcula el area lateral de un prisma reatangular
def area_lat_prism(ancho,largo,altura):
    area_lat=2*(ancho+largo)*altura
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
    potencia=base**exponente
    return potencia
#Fin_def

#24. Funcion que la fuerza de un cuerpo
def fuerza(masa,aceleracion):
    force=masa*aceleracion
    return force
#Fin_def

#25. Funcion que calcula la suma de los n primeros cuadrados perfectos
def sum_cuadrados(n):
    sumatt=(n**2+n)(2*n+1)/6
    return sumatt
#Fin_def






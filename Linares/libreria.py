#1. Presion hidrostatica
def presion_hidrostatica(densidad, gravedad, altura):
    resultado=(densidad*gravedad*altura)
    return resultado
#fin_def

#2. Fuerza de una maquina
def fuerza_de_maquina(masa, aceleracion):
    resutado=(masa*aceleracion)
    return resutado
#fin_def

#3. formula del area lateral de un prisma
def area_lateral_de_un_prisma(perimetro_de_la_base, arista):
    resutado=(perimetro_de_la_base*arista)
    return resutado
#fin_def

#4. Formula del volumen de un prisma
def volumen_prisma(area_de_la_base, altura):
    resutado=area_de_la_base*altura
    return resutado
#fin_def

#5. Volumen de un rectoedro
def volumen_rectoedro(base_menor, base_mayor, altura):
    resutado=base_mayor*base_menor*altura
    return resutado
#fin_def

#6. Area lateral de un cono
def area_lateral_de_un_cono(pi, radio,altura):
    resutado=pi*radio*altura
    return resutado
#fin_def

#7. area de una esfera
def area_de_una_esfera(pi, radio):
    resutado=(pi*radio*radio)*4
    return resutado
#fin_def

#8. Area de una zona esferiaca
def zona_esferica(pi,radio,altura):
    resutado=(pi*radio*altura)*2
    return resutado
#fin_def

#9. Fuerza electrostatica
def fuerza_electrostatica(carga, campo_electrico):
    resutado=carga*campo_electrico
    return resutado
#fin_def

#10. Diferencia de ptencial
def diferencia_de_potencial(resistencia, corriente):
    resutado=resistencia*corriente
    return resutado
#fin_def

#11. Variacion de energia interna
def variacion_de_energia_interna(calor, trabajo):
    resutado=calor*trabajo
    return resutado
#fin_def

#12 Trabajo
def trabajo(fuerza, distancia):
    resutado=fuerza*distancia
    return resutado
#fin_def

#13. Aceleracion angular
def aceleracion_angular(velocidad_angular, radio):
    resutado=(velocidad_angular*velocidad_angular*radio)
    return resutado
#fin_def

#14. Formula de densidad
def densidad(masa, volumen):
    resutado=masa/volumen
    return resutado
#fin_def

#15. Formula de presion
def presion(masa, aceleracion, area):
    resutado=masa*aceleracion/area
    return resutado
#fin_def

#16. Empuje de un liquido
def empuje_de_un_liquido(densidad, gravedad, volumen):
    resutado=densidad*gravedad*volumen
    return resutado
#fin_def

#17. Formula de la energia potencial gravitatoria
def energia_pot_grav(masa, gravedad, altura):
    resutado=masa*gravedad*altura
    return resutado
#fin_def

#
def pedir_rango(msg, r1, r2):
    rango_invalido=True
    valor=0
    while(rango_invalido):
        valor=pedir_rango(msg)
        rango_invalido=(valor<r1 or valor>r2)
        #fin_while
        return valor

#fin_def

#18. Edad en un rango de 1 a 100 años
def pedir_edad(msg):
    return pedir_rango(msg, 1, 100)
#fin_def

#19. Temperatura corporal en un rango de 35 a 39 grados
def pedir_temperatura_corporal(msg):
    return pedir_rango(msg, 35, 39)
#fin_def

#20. Notas de fin de ciclo
def pedir_notas_de_fin_de_ciclo(msg):
    return pedir_rango(msg, 0, 20)
#fin_def
def promedio(n1, n2):
    valor=(n1+n2)/2
    return valor

#21 Area de un rectangulo
def pedir_area_de_un_rectangulo(base, altura):
    valor=base*altura
    return valor
#fin_def

#22. Velocidad final
def velocidad_final(velocidad_inicial, aceleracion, distancia):
    resutado=(velocidad_inicial+ 2*(aceleracion) + distancia)
    return resutado
#fin_def

#23 Velocidad Tangencial
def velocidad_tangencial(velocidad_angular, radio):
    resutado=(velocidad_angular*velocidad_angular*radio*radio)
    return resutado
#fin_def

#24 Fuerza de rozamiento
def fuerza_de_rozamiento(u, n):
    resutado=(u*n)
    return resutado
#fin_def

#25 Formula de dilatacion superficial
def dilatacion_superficial(area_inical, beta, variacion_de_temperatura):
    resutado=(area_inical*beta*variacion_de_temperatura)
    return resutado
#fin_def

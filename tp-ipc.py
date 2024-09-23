#Los Colores
#Fecha de Entrega: 11 de octubre.

'''
Un número pseudoaleatorio es un número generado en un 
proceso que parece producir números al azar, 
pero no lo hace realmente.

OBJETIVO: Ganar el peluche mas grande posible. 
    lista: con nombre y puntajes.
    para ganar, tener el puntaje con > puntuacion.
'''

import random 

print("Bienevenidos al parque de diviersiones!")
print("Estaras jugando a \"Adivina el Color\"")
print("Aqui cada numero del 1 al 9 representa un color")
print("?Cuantas botellas quiere adivinar? Tenga en cuenta que por cada botella que deba adivinar puede sumar 1000 puntos")

cantidad_de_botellas_ingresadas= int(input("Ingrese la cantidad: "))

print(f"Exelente, los numeros del 1 al {cantidad_de_botellas_ingresadas} han sido ordenados aleatoriamente.")
print("Usted debera adivinar ese oreden en 10 intentos. Por cada numero adivinado ganara 1000 puntos")
print("Por cada intento perdido perdera 100 puntos")
print("Tambien puede pedir ayuda escribiendo \"help\". Esta ayuda le revelara uno de los numeros.")
print("Tenga en cuenta que por cada ayuda que pida perdera un intento (-100) y no ganara puntos por ese numero.")

'''Creamos el orden de botellas a adivinar por el participante'''
solucion= " "
while len(solucion) < cantidad_de_botellas_ingresadas:
    num= str(random.randint(1, cantidad_de_botellas_ingresadas))
    if num not in solucion:
        solucion+= num
print(solucion)
#-------------------------------------------------------------------------------------
'''Contadores para ir restando el numero de intentos'''
intentos_totales = 10
intentos_restantes= intentos_totales 

'''Contadores para ir sumando o restando los puntos'''
puntaje_por_botella= cantidad_de_botellas_ingresadas*1000
puntos_negativos= intentos_totales* -100
puntaje_total = 0

'''Contador para el numero de botellas acertadas'''
botellas_correctas= 0

i= "iniciar el bucle"
while i == "iniciar el bucle":
    adivinanza= input("Ingrese su adivinanza: ")

    if len(adivinanza) != cantidad_de_botellas_ingresadas:
        print("La longitud no es la corresta")
        continue
    posicion_correcta=0
    
    for x in range(cantidad_de_botellas_ingresadas):
        if solucion[x] == adivinanza[x]:
            posicion_correcta+=1
            if posicion_correcta == cantidad_de_botellas_ingresadas:
                print("congrants")
            else: 
                print(f"adivinaste {posicion_correcta}")
    '''if adivinanza in solucion:
        correctos= 2
        intentos_totales-=1
        print(f"Tiene {correctos}.Le quedan {intentos_restantes} intentos")
    if adivinanza == "help":
        print(f"Un numero aleatorio es: {random.randint(1, cantidad_de_botellas_ingresadas)}")
        intentos_totales -= 1
        adivinanza= input("Ingrese su adivinanza: ")
        continue
        
    if intentos_totales <= 0:
        print(f"Tiene {correctos}. Le quedan {intentos_restantes} intentos")
        print(f"Ha perdido, la respuesta era {solucion}")
        break
print(f"Tiene {correctos}. Le quedan {intentos_restantes} intentos")
print("Felicidades, ha adivinado todas!")
print(f"Tiene un puntaje de {puntaje_total}")'''

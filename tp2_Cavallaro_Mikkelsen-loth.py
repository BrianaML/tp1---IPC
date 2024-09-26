#TP - Los Colores
#Fecha de Entrega: 11 de octubre.
#Hecho por: Maria Agustina Cavallaro y Briana Mikkelsen-loth

import random 
#Explicacion de reglas del juego + pedida de numero de botellas que aspira adivinar
print("Bienevenidos al parque de diversiones!")
print("Estaras jugando a \"Adivina el Color\"")
print("Aqui cada numero del 1 al 9 representa un color")
print("¿Cuantas botellas quiere adivinar? Tenga en cuenta que por cada botella que deba adivinar puede sumar 1000 puntos")

cantidad_de_botellas_ingresadas= int(input("Ingrese la cantidad: "))

print(f"Excelente, los numeros del 1 al {cantidad_de_botellas_ingresadas} han sido ordenados aleatoriamente.")
print("Usted debera adivinar ese oreden en 10 intentos. Por cada numero adivinado ganara 1000 puntos ;)")
print("Por cada intento perdido perdera 100 puntos :(")
print("Tambien puede pedir ayuda escribiendo \"help\". Esta ayuda le revelara uno de los numeros.")
print("Tenga en cuenta que por cada ayuda que pida perdera un intento (-100) y no ganara puntos por ese numero.")

# Creamos el orden de botellas a adivinar por el participante
solucion=""
while len(solucion) < cantidad_de_botellas_ingresadas:
    num= str(random.randint(1, cantidad_de_botellas_ingresadas))
    if num not in solucion:
        solucion+= num

# VARIABLES Y CONTADORES NECESARIOS PARA EL JUEGO
# Contadores para ir restando el numero de intentos
intentos_totales = 10
intentos_restantes= intentos_totales 

# Contadores para ir sumando o restando los puntos
puntaje_por_botella= cantidad_de_botellas_ingresadas*1000
puntos_negativos= 0 
puntaje_total = 0

#Contadores para Help
ayuda_usada=[] #Creamos una lista vacia
for i in range(cantidad_de_botellas_ingresadas):
    ayuda_usada.append(False)
revelacion= [] #Creamos una lista vacia
for i in range(cantidad_de_botellas_ingresadas):
    revelacion.append(" _ ")

#BUCLE DEL JUEGO
while intentos_totales > 0:
    adivinanza= input("Ingrese su adivinanza: ")
    #HELP ----
    if adivinanza.lower() == "help":
        for i in range(cantidad_de_botellas_ingresadas):
            if not ayuda_usada[i]:
                revelacion[i]= solucion[i]
                ayuda_usada[i]= True
                revelacion_str= " " #Inicializa la cadena vacia ----------
                
                for caracter in revelacion:
                    revelacion_str+= caracter
                    
                print(f"Revelacion: {revelacion_str}. Le quedan {intentos_totales-1} intentos")
                intentos_totales-=1
                puntos_negativos+=1100 #Penalizamos por pedir ayuda
                break
        continue    
    
    # Se "penaliza" al user por no ingresar la longitud correcta o estar repetido
    if len(adivinanza) != cantidad_de_botellas_ingresadas:
        intentos_totales-= 1
        puntos_negativos+=100
        
        puntaje_total= puntaje_por_botella - puntos_negativos
        intentos_restantes= intentos_totales
        
        print("El numero ingresado no contiene todos los numeros del juego o es muy largo.")
        print(f"Pierde el turno. Le quedan {intentos_restantes} intentos")
        continue
    
    numero_de_botellas_ingresadas=[]
    repetido= False #un stop por si encontramos un valor repetido.
    
    for botella in adivinanza:
        if botella in numero_de_botellas_ingresadas:
            repetido= True
            break
        numero_de_botellas_ingresadas.append(botella)
    
    if repetido:
        intentos_totales-=1
        puntos_negativos+=100
        
        puntaje_total= puntaje_por_botella - puntos_negativos
        intentos_restantes= intentos_totales
        print("La adivinanza ingresada tiene numeros repetidos.")
        print(f"Pierde el turno. Le quedan {intentos_restantes} intentos")
        continue
    
    #Contador para el numero de botellas acertadas
    botellas_correctas= 0
    posicion_correcta=0

    for x in range(cantidad_de_botellas_ingresadas):
        if solucion[x] == adivinanza[x]:
            posicion_correcta+=1
            botellas_correctas+=1
            
    intentos_totales-=1
    intentos_restantes=intentos_totales
    # Por cada intento fallido o pedida de ayuda, se le restan puntos al user
    if posicion_correcta != cantidad_de_botellas_ingresadas:
        puntos_negativos+=100
    
    puntaje_total= puntaje_por_botella - puntos_negativos
    
    # Caso user gane, termina el juego adivinando todos los numeros, se muestra el puntaje alcanzado
    if posicion_correcta == cantidad_de_botellas_ingresadas:
        print(f"Tiene {botellas_correctas} correctos. Le quedan {intentos_restantes} intentos")
        print("Felicidades, ha adivinado todas!")
        print(f"Tiene un puntaje de {puntaje_total}")
        break
    else: 
        print(f"Tiene {botellas_correctas} correctos. Le quedan {intentos_restantes} intentos")
    
    # Caso user pierda, se le acaban los intentos, se termina el juego y se muestra cual era el orden correcto
if intentos_totales == 0:
    #print(f"Tiene {botellas_correctas}. Le quedan {intentos_restantes} intentos")
    print(f"Ha perdido, la respuesta era {solucion}")
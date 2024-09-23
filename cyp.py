import random 

# Explicación del juego 
print("Bienvenidos al parque de diversiones!") 
print("Estás jugando a \"Adivina el Color\"") 
print("Aquí, cada número del 1 al 9 representa un color.") 
print("¿Cuántas botellas quieres adivinar? Por cada botella correcta puedes sumar 1000 puntos.") 
print("Por cada intento fallido, perderás 100 puntos.") 
print("Puedes pedir ayuda escribiendo \"help\", lo que revelará un número pero te costará un intento y no ganarás puntos por esa botella.") 

# El usuario decide cuántas botellas quiere jugar 
cantidad_de_botellas = int(input("Ingrese la cantidad de botellas con las que desea jugar: "))

print(f"Excelente, los numeros del 1 al {cantidad_de_botellas} han sido ordenados aleatoriamente.")
print("Usted debera adivinar ese oreden en 10 intentos. Por cada numero adivinado ganara 1000 puntos") 
print("Por cada intento perdido perdera 100 puntos") 
print("Tambien puede pedir ayuda escribiendo \"help\". Esta ayuda le revelara uno de los numeros.") 
print("Tenga en cuenta que por cada ayuda que pida perdera un intento (-100) y no ganara puntos por ese numero.") 

# Se genera la solución aleatoria 
solucion = "" 
while len(solucion) < cantidad_de_botellas: 
    num = str(random.randint(1, cantidad_de_botellas)) 
    if num not in solucion: 
        solucion += num 
        
# Variables y contadores necesarios para el juego 
intentos_totales = 10 
intentos_restantes = intentos_totales 

puntaje_por_botella = 1000 
puntos_negativos = 0 
puntaje_total = 0 

ayuda_usada = False 
juego_terminado = False 

# Bucle principal del juego 
while intentos_restantes > 0 and not juego_terminado: 
    print(f"\nTienes {intentos_restantes} intentos restantes") 
    
    # Preguntar por ayuda (solo si no se ha usado) 
    if not ayuda_usada: 
        pedir_ayuda = input("¿Deseas pedir ayuda para ver la botella correcta de la izquierda? (s/n): ") 
        if pedir_ayuda.lower() == "s": 
            print("Pidiendo ayuda pierdes 100 puntos y un intento") 
            print(f"La primera botella correcta es {solucion[0]}") 
            ayuda_usada = True 
            intentos_restantes -= 1 
            
            # Pierdes un intento por pedir ayuda 
            puntos_negativos += 100 
            
            # Se restan puntos por pedir ayuda 
            if intentos_restantes > 0: # Solo si no se agotaron los intentos por pedir ayuda 
            # Entrada de la adivinanza 
                adivinanza = input(f"Ingrese su adivinanza ({cantidad_de_botellas} números): ") 
                # Validar que la longitud de la adivinanza sea correcta 
                if len(adivinanza) != cantidad_de_botellas: 
                    print(f"Error: Debes ingresar {cantidad_de_botellas} números.") 
                    intentos_restantes -= 1 
                    puntos_negativos += 100 
                else: 
                # Comprobar si la adivinanza tiene números repetidos 
                    if len(set(adivinanza)) != len(adivinanza): 
                        print("Error: La adivinanza tiene números repetidos.") 
                        intentos_restantes -= 1 
                        puntos_negativos += 100 
            else:
            # Contar cuántas botellas son correctas y construir la cadena de botellas acertadas
                botellas_correctas = 0
                botellas_acertadas = ""  # Guardar las botellas correctas
                for i in range(cantidad_de_botellas):
                    if adivinanza[i] == solucion[i]:
                        botellas_correctas += 1
                        botellas_acertadas += adivinanza[i] + " "  # Añadir la correcta con espacio
                    else:
                        botellas_acertadas += "_ "  # Añadir guión bajo para incorrectas
            # Si adivinó todas las botellas, el jugador gana
                if botellas_correctas == cantidad_de_botellas:
                    print("¡Felicidades! Adivinaste todas las botellas.")
                    puntaje_total = (botellas_correctas * puntaje_por_botella) - puntos_negativos
                    print(f"Tu puntaje total es: {puntaje_total}")
                    juego_terminado = True
                else:
                    # Si no adivinó todas las botellas, pierde un intento y se restan puntos
                    intentos_restantes -= 1
                    puntos_negativos += 100
# Si se agotaron los intentos y no ganó, mostrar la solución
if not juego_terminado:
    print(f"\nLo siento, te quedaste sin intentos. La solución era: {solucion}")
    puntaje_total = (botellas_correctas * puntaje_por_botella) - puntos_negativos
    print(f"Tu puntaje final es: {puntaje_total}")
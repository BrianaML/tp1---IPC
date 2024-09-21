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


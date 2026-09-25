# Escribe un programa que calcule el área de un círculo. El programa deberá pedir al usuario que introduzca el radio del círculo y, utilizando la fórmula Área = Pi * radio^2.
import math

keepAsking = True

while keepAsking == True:
	try:
		radius = float(input("Introduce the circle radius:"))
		print("The circle area is", math.pi * radius ** 2)

		keepAsking = False
	except ValueError:
		print("Error: Caracter introduced wasn't a number.")

# Pedir dos números enteros y hacer el primer número módulo el segundo número.

keepAsking = True

while keepAsking == True:
	try:
		number1 = int(input("Introduce an integer number:"))
		number2 = int(input("Introduce another integer number:"))
		print("The module of both numbers is:", number1 % number2)
		keepAsking = False
	except ValueError:
		print("Error: Caracter introduced wasn't an integer number.")

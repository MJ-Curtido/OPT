# Escribe un programa que pida al usuario dos números reales (decimales) y calcule su suma.

keepAsking = True

while keepAsking == True:
	try:
		number1 = float(input("Introduce a number:"))
		number2 = float(input("Introduce another number:"))
		print("The sum of both numbers is:", number1 + number2)
		keepAsking = False
	except ValueError:
		print("Error: Caracter introduced wasn't a number.")

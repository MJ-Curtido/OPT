# Diseña un programa que solicite dos números reales y muestre el resultado de multiplicarlos entre sí.

keepAsking = True

while keepAsking == True:
	try:
		number1 = float(input("Introduce a number:"))
		number2 = float(input("Introduce another number:"))
		print("The multiplication of both numbers is:", number1 * number2)
		keepAsking = False
	except ValueError:
		print("Error: Caracter introduced wasn't a number.")

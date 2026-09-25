# Realiza un programa que pida dos números enteros al usuario y devuelva el producto de ambos.

keepAsking = True

while keepAsking == True:
	try:
		number1 = int(input("Introduce an integer number:"))
		number2 = int(input("Introduce another integer number:"))
		print("The multiplication of both numbers is:", number1 * number2)
		keepAsking = False
	except ValueError:
		print("Error: Caracter introduced wasn't an integer number.")

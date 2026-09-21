keepAsking = True

while keepAsking == True:
	try:
		number1 = int(input("Introduce a number:"))
		number2 = int(input("Introduce another number:"))
		print("La suma de ambos número es:", number1 + number2)
		keepAsking = False
	except ValueError:

		print("Error: Caracter introduced wasn't a number.")

# Crea un programa que convierta metros a centímetros. El programa deberá pedir al usuario que introduzca una cantidad en metros y devolver la cantidad en centímetros.

keepAsking = True

while keepAsking == True:
	try:
		meter = float(input("Introduce an integer number:"))
		if meter == 1:
			print(meter, "meter are", meter * 100, "centimeters.")
		else:
			print(meter, "meters are", meter * 100, "centimeters.")

		keepAsking = False
	except ValueError:
		print("Error: Caracter introduced wasn't a number.")

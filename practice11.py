# Escribe un programa que calcule el importe total a pagar en un restaurante. El programa deberá pedir al usuario el coste de la comida y el porcentaje de propina que quiere dejar, y luego devolver el importe total.

def restaurantCost():
	keepAsking = True

	while keepAsking == True:
		try:
			cost = float(input("Introduce the food cost:"))
			if cost < 0: raise type("NegativeException", (Exception,), {})("The food cost can't be negative")
			percentage = float(input("Introduce the tips percentage you'd like to pay:"))
			if percentage < 0: raise type("NegativeException", (Exception,), {})("The food percentage can't be negative")
			print("The total cost are", cost * (percentage / 100 + 1))

			keepAsking = False
		except ValueError:
			print("Error: Caracter introduced wasn't a number.")
		except Exception as e:
			print(e)

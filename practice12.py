# Crea un programa que calcule el IMC (Índice de Masa Corporal) del usuario. El programa deberá pedir al usuario su peso (en kilogramos) y su altura (en metros), y luego calcular su IMC usando la fórmula: IMC = Peso / Altura^2.

def bmiCalculator():
	keepAsking = True

	while keepAsking == True:
		try:
			weight = float(input("Introduce your weight (kg):"))
			if weight < 0: raise type("NegativeException", (Exception,), {})("Your weight can't be negative")
			height = float(input("Introduce your height (m):"))
			if height < 0: raise type("NegativeException", (Exception,), {})("Your height can't be negative")
			print("Your BMI is ", weight / height ** 2)

			keepAsking = False
		except ValueError:
			print("Error: Caracter introduced wasn't a number.")
		except Exception as e:
			print(e)

#14. Enunciado: Meter en un match / case los ejercicios del 9 al 13, de forma que aparezca un menú con las 5 opciones para que el usuario decida que ejercicio o enunciado quiere ejecutar.
#15. Añadir al ejercicio anterior una opción para salir del programa y un bucle del que sólo saldrá el programa cuando el usuario seleccione dicha opción de salida.
#16. Añade al ejercicio anterior un control de errores o control de excepciones con try/except, incluye reglas de negocio con raise, por ejemplo una distancia en metros no puede ser negativa y las excepciones de ValueError y ZeroDivisionError.

from practice1 import sumNumbers
from practice2 import sumFloat
from practice3 import substraction
from practice4 import multiplication
from practice5 import multiplicationFloat
from practice6 import division
from practice7 import divisionFloat
from practice8 import module
from practice9 import metersToCentimeters
from practice10 import circleArea
from practice11 import restaurantCost
from practice12 import bmiCalculator
from practice13 import welcome

keepAsking = True

while keepAsking == True:
	try:
		print("\n\n")
		
		print("Choose an option:\n\t1. Sum.\n\t2. Sum float.\n\t3. Substraction.\n\t4. Multiplication.\n\t5. Multiplication float.\n\t6. Division.\n\t7. Division float.\n\t8. Module.\n\t9. Meters to centimeters.\n\t10. Circle area.\n\t11. Restaurant cost.\n\t12. BMI calculator.\n\t13. Welcome.\n\n\t14. Exit")
		option = int(input("Introduce an option:"))
		
		if option < 1 or option > 14: raise type("valueException", (Exception,), {})("Introduce a valid option.")
		
		print("\n")

		match option:
			case 1:
				sumNumbers()
			case 2:
				sumFloat()
			case 3:
				substraction()
			case 4:
				multiplication()
			case 5:
				multiplicationFloat()
			case 6:
				division()
			case 7:
				divisionFloat()
			case 8:
				module()
			case 9:
				metersToCentimeters()
			case 10:
				circleArea()
			case 11:
				restaurantCost()
			case 12:
				bmiCalculator()
			case 13:
				welcome()
			case 14:
				print("Goodbye!!")
				keepAsking = False

		print("\n\n")

	except ValueError:
		print("Error: Caracter introduced wasn't a number.")
	except Exception as e:
		print(e)

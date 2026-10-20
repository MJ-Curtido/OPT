# ------- 1. Lista -------
print('1. Lista\n')

games = [["Minecraft", 30], ["Hollow Knight", 20], ["EuroTruck Simulator", 5]]
games.append(["Raft", 15])

for game in games:
	print(f'{game[0]}: {game[1]}€')

# ------- 2. Tupla -------
print('\n\n\n')
print('2. Tupla\n')

subjects = ('Sostenibilidad', 'Despliegue', 'Diseño', 'Desarrollo cliente', 'Desarrollo servidor', 'Inglés', 'Digitalización', 'Proyecto', 'Optativa')

print('Asignaturas:')
# No es modificable, asi que no se pueden añadir elementos ni modificar nada del mismo
for subject in subjects:
	print(f"\t- {subject}")

# ------- 3. Dicctionario clave-valor -------
print('\n\n\n')
print('3. Diccionario clave-valor\n')

discounts = {"Nuevo con etiqueta": 0, "Nuevo sin etiqueta": 5, "Buen estado": 10, "Usado": 20}
discounts["Mal estado"] = 50

print('Descuentos según estado:')
for key, value in discounts.items():
	print(f"\t- {key}: {value}%")

# ------- 4. Diccionario solo claves -------
print('\n\n\n')
print('4. Diccionario solo claves\n')

levels = {"Junior": ["Manu", "Lidia"]}
levels.setdefault("Junior", []).append("Álvaro")
levels.setdefault("Senior", []).append("Secundino")

print('Empleados empresa:')
for key in levels:
	print(f"\t- {key} —> {levels[key]}")

# ------- 5. Diccionario solo valores -------
print('\n\n\n')
print('5. Diccionario solo valores\n')

people = {"Manu": 24, "Lidia": 29, "Adrián": 18}
sumatory = 0

print('Edades:')
for age in people.values():
	sumatory += age

	print(f'- {age}')

print(f'\nMedia de edad: {round(sumatory / len(people), 2)}')

# ------- 6. Cadena de caracteres -------
print('\n\n\n')
print('6. Cadena de caracteres\n')

text = "Hello"
text += " World"

for letter in text:
	print(letter * 2)

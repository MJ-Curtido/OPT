sales = [('Apple', 3, 2.7), ('Tangerine', 7, 1), ('Custard apple', 2, 7), ('Mango', 1, 9), ('Watermelon', 4, 5)]

sum = 0

print('Fruits selled:')
for sale in sales:
	total = round(sale[1] * sale[2], 2)

	print(f"\t- {sale[0].upper()} --> total: {total}")

	sum += total

print(f"\n\nTotal amount: {sum}")

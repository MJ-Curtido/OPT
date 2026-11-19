import pandas as pd

FILE_PATH = "Ej_27_Pandas_1.xlsx"
SHEET_NAME = "Alumnos"
data = {}
data_dict = {}
data_index = {}
data_list = {}

fileDB = pd.ExcelFile(FILE_PATH)
dataframe = pd.read_excel(fileDB, sheet_name=SHEET_NAME, index_col=None)
dataframe.fillna("")
print(dataframe)

""" Opción con orient='records' """
print("------- RECORDS -------")
data[SHEET_NAME] = dataframe.to_dict(orient='records')
print(data)

for element in data[SHEET_NAME]:
	for key, value in element.items():
		print(f'\t{key}: {value}')
	print('\n---\n')

""" Opción con orient='dict' """
print("------- DICT -------")
data_dict[SHEET_NAME] = dataframe.to_dict(orient='dict')
print(data_dict)

for column, row in data_dict[SHEET_NAME].items():
	print(f'- {column}')
	for key, value in row.items():
		print(f'\t{key}: {value}')
	print('\n---\n')

""" Opción con orient='index' """
print("------- INDEX -------")
data_index[SHEET_NAME] = dataframe.to_dict(orient='index')
print(data_index)

for element in data_index[SHEET_NAME].values():
	for key, value in element.items():
		print(f'\t{key}: {value}')
	print('\n---\n')

""" Opción con orient='list' """
print("------- LIST -------")
data_list[SHEET_NAME] = dataframe.to_dict(orient='list')
print(data_list)

for key, value in data_list[SHEET_NAME].items():
	for key, value in element.items():
		print(f'\t{key}: {value}')
	print('\n---\n')

print("-------------- RECORRIENDO CON INDEX_COL=0 --------------")

df_index = pd.read_excel(fileDB, sheet_name=SHEET_NAME, index_col=0)
df_index.fillna("")
print(df_index)

""" Opción con orient='dict' """
print("------- DICT CON ID_PERSONA -------")
data_dict_id = df_index.to_dict(orient="dict")
print(data_dict_id)

for column, row in data_dict_id.items():
	print(f'- {column}')
	for key, value in row.items():
		print(f'\t{key}: {value}')
	print('\n---\n')

""" Opción con orient='index' """
print("------- INDEX CON ID_PERSONA -------")
data_index_id = df_index.to_dict(orient='index')
print(data_index_id)

for id_person, data_person in data_index_id.items():
	print(f"- Alumno: {id_person}")

	for key, value in data_person.items():
		print(f'\t{key}: {value}')
	print('\n---\n')

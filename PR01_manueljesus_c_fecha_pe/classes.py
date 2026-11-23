class Alumno():
	def __init__(self, id:str, email:str):
		self.id = id
		self.email = email

	@property
	def id(self) -> str:
		return self.id

	@id.setter
	def id(self, value:str) -> None:
		self._id = value

	@property
	def email(self) -> str:
		return self.email

	@email.setter
	def email(self, value:str) -> None:
		if value.endswith('@g.educaand.es'):
			self._email = value
		else:
			#TODO: Control de errores si el email no es correcto
			pass

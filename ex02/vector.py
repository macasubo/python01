class Vector:
	def __init__(self, coord):
		if type(coord) == type(list()):
			self.values = coord
			self.size = len(coord)
		elif type(coord) == type(int):
			self.size = coord
			self.values = list()
			for i in coord:
				self.values.append(float(i))
		elif type(coord) == type(tuple):
			self.size = coord[1] - coord[0]
			self.values = list()
			for i in coord:
				self.values.append(float(i))

	def __repr__(self):
		return f'Object: size: {self.size}, values: {self.values}'

	def __str__(self):
		return ', '.join([f'{key}: {value}' for key, value
											in self.__dict__.items()])

	def __add__(v1, v2):
#		result = list()
		return [v1.values[i] + v2.values[i] for i in v1.size]

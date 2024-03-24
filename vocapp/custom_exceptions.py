
class EmptyQuery(Exception):
	def __init__(self, error):
		self.error = error

	def __str__(self):
		if self.error == 0:
			return f'Empty query error ({self.error}): Unknown error.'
		if self.error == 1:
			return f'Empty query error ({self.error}): No expressions to review.'
		elif self.error == 2:
			return f'Empty query error ({self.error}): No expressions to discover.'
		elif self.error == 3:
			return f'Empty query error ({self.error}): No expressions in the database, oh no...'
		elif self.error == 4:
			return f'Empty query error ({self.error}): No phrasal verb expressions found.'
		elif self.error == 5:
			return f'Empty query error ({self.error}): No expressions found.'
		elif self.error == 6:
			return f'Empty query error ({self.error}): No phrasal verb expressions found with the selected level filters.'
		elif self.error == 7:
			return f'Empty query error ({self.error}): No expressions found with the selected level filters.'
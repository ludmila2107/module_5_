class Home:
	def __init__(self, number_of_floors, color, year = 12) :
		self.number_of_floors = number_of_floors
		self.color = color
		self.year = year
	def change_color(self, new_color):
		self.color = new_color
	def change_year(self, new_year):
		self.year = new_year

home1 = Home(5, 'pink')
# print(dir(home1))
print(home1.number_of_floors)
print(home1.color)
print(home1.year)
home1.change_year(56)
print(home1.year)
home1.change_color('red')
print(home1.color)

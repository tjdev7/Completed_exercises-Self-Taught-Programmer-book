#OOP - object oriented programming - instantiating a class - creating an object 4
class Orange:
	def __init__(self, w, c):
		self.weight = w
		self.color = c
		print("Created!")


or1 = Orange(10, "light orange")
or2 = Orange(8, "dark orange")
or3 = Orange(14, "yellow")


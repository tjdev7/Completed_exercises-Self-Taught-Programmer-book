#OOP - object oriented programming - instantiating a class - creating an object 1
class Orange:
	def __init__(self, w, c):
		self.weight = w
		self.color = c
		print("Created!")


or1 = Orange(10, "dark orange")
print(or1)
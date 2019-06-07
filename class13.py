# overloading

class OverloadingTest:
	def __init__(self, tm):
		self.num = tm
	def show_data(self):
		print("self.num : ", self.num)
	def __add__(self, de):
		self.num +=  de
	def __radd__(self, de):
		self.num +=  de
	def __sub__(self,de):
		self.num -= de


mycls = OverloadingTest(50)
mycls.show_data()

# operator overloading(+)
mycls.__add__(30) 	# @cpp 	  : mycls.operator+(30)
					# @python : mycls.__add__(30)
mycls.show_data()
# operator overloading(-)
mycls.__sub__(30)
mycls.show_data()
# reverse  add
20 + mycls
mycls.show_data()
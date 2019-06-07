class Test2():
	var = 78
	def __init__(self, data):
		self.var = data
		print("_init_ self.var :", self.var)

	def method1(self):
		print("method1 Test2.var : ", Test2.var)
		print("method1 self.var : ", self.var)

# decorator
	@classmethod
	def chage_data(cls,de):
		cls.var = de

inst = Test2(50)
print("inst var : ",inst.var)

inst3 = Test2(60)
print("inst3 var : ",inst3.var)

inst.method1()
inst3.method1()

Test2.chage_data(217)
print("Test2.var : ",Test2.var)
Test2.var = 33
print("Test2.var : ", Test2.var)
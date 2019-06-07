# book page 371
# instace로 접근할 때에는 scoping rule을 따르지만, method(member function)으로 접근 할때에는 전역변수부터 찾음.
var = 777

class Test2():
	#var = 777	
	def method1(self):
		print(var)

inst = Test2()
inst.method1()
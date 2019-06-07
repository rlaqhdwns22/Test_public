# diff. var.

var = 0 	# global var.

class myclassTest():
	var = 78 	# class attribute var.
	def __init__(self, data):
		var =20 	# local var.
		self.var = data 	# instance var.
	def show_data(self):
		print("self.var : ",self.var)

mytest = myclassTest(30)

print(var)
print(myclassTest.var)
print(mytest.var)

mytest.show_data()

# edit calss att. var. : directly
myclassTest.var = 22
print(myclassTest.var)

print(dir(mytest)) # show objects available access

mytest.modify = 88 # add modify var.
print(dir(mytest))
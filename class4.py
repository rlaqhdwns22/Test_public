# find var.
# instance var. -> attribute var. -> global var
# : scoping rule

class HouseClass():
	Company = "python Academy"
	def __init__(self, year, address, price):
		self.year = year
		self.address = address
		self.price = price
	def show_company(self):
		print(self.Company)
	def change_company(self,name):
		self.Company = name
	def show_info(self):
		print("""This house is built by {},
			in {}
			address : {}
			price : {} """
			.format(self.Company, self.year, self.address, self.price))

if __name__ == "__main__":
	houseA = HouseClass(2019,"Guro",34.56)
	houseA.show_company()

	houseA.change_company("MDS Academy")	# make new instance var.
	houseA.show_company()
	houseA.show_info()

	houseB = HouseClass(2020,"pankyo",999.99)
	houseB.show_info()
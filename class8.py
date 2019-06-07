class HouseClass():
	Company = "python Factory"
	def __init__(self, year, address, price):
		self.year = year
		self.address = address
		self.price = price
	@classmethod
	def show_company(cls):
		print(cls.Company)
	@classmethod
	def Change_company(cls,name):
		cls.Company = name
	def show_info(self):
		print("""This house was built by {} in {}, address : {}, price : {} """
			.format(HouseClass.Company, self.year, self.address, self.price))

houseA = HouseClass(2019, "Guro", 34.56)
houseA.show_company()
houseA.Change_company("MDS Academy")
houseA.show_company()

houseA.show_info()

houseB = HouseClass(2020, "pangyo", 999.99)
HouseClass.Company = "Hancommds"
houseB.show_info()
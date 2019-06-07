class Account():
	def __init__(self, money):
		self.balance = money
	def deposit(self, money):
		self.balance += money
	def withdraw(self, money):
		self.balance -= money
	def show_Account(self):
		print("balance : {} Won".format(self.balance))

class fixed_Account(Account):
	def deposit(self, money):	# overriding
		self.balance += money*1.07
	def withdraw(self, money):	# overriding
		self.balance -= money + 10

class fund_Account(Account):
	def deposit(self, money):	# overriding
		self.balance += money*2.17
	def withdraw(self, money):	# overriding
		self.balance -= money + 150

class stock_accout(Account):
	def __init__(self, name, money):
		#Account.__init__(self, money)
		super().__init__(money)
		self.name = name
	def deposit(self, money):
		self.balance += money * 1.37
	def withdraw(self, money):
		self.balance -= money + 50
	def show_Account(self):
		print("Account owner : {}".format(self.name))
		super().show_Account()


# myact = Account(100)
# myact.show_Accout()
# myact.deposit(100)
# myact.show_Accout()
# myact.withdraw(150)
# myact.show_Accout()

myyellowact = fixed_Account(100)
myyellowact.deposit(200)
myyellowact.show_Account()
myyellowact.withdraw(150)
myyellowact.show_Account()

myyellowact = fund_Account(100)
myyellowact.deposit(200)
myyellowact.show_Account()
myyellowact.withdraw(150)
myyellowact.show_Account()

myact = stock_accout("MDS", 500)
myact.deposit(200)
myact.show_Account()
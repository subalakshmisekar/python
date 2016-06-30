class BankAccount(object):
	def __init__(self,money):
		self.money = money
		print 'Init Account'

	def showMoney(self):
		print self.money

	def addName(self,name):
		self.name = name

b1 = BankAccount(100)
b1.addName('abc')
b1.showMoney()
print b1.showMoney()
print b1.name
b2 = BankAccount(200)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
print b2.showMoney()

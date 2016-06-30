#classes & objects

class BankAccount(object):
	def _init_(self,money):
	    self.money = money
	    print 'Init Account'
	def showMoney(self):
	    print self.money
	def addName(self,name):
	    self.name = name


b1 = BankAccount(100)
b1.addName('abc')
b1.showMoney()
print b1.name

b2 = BankAccount(200)
b2.showMoney()


print b1, b2

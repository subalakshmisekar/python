class Mango(object):
	def __init__(self,price,market):
		self.price = price
		self.market = market

class Apple(object):
	def __init__(self,price,location):
		self.price = price
		self.location = location

	def __eq__(self,x):
		if isinstance(x,Orange):
			return self.price == x.price and self.location == x.location
		else:
			return self.price == x.price


class Orange(object):
	def __init__(self,price,address):
		self.price = price
		self.location = address 

a = Apple(100, 'chennai')
m = Mango(100, 'bangalore')
o = Orange(100, 'chennai')

if a == m:
	print 'Same'
else:
	print 'Not Same'

if a == o:
	print 'same'
else:
	print 'not same'
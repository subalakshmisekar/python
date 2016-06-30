class Person(object):
	def __init__(self,name,idCard):
		self.name = name
		self.id = idCard
		

	def __repr__(self):
		return self.name + " " + self.id

	def __hash__(self):
		return hash(self.name)

	def __eq__(self,x):
		return self.name == x.name and self.id == x.id

db = { Person('abc','abc445') : 'abc@jbn.com',
	   Person('def','def778') : 'def@jbn.com',
	   Person('ghi','ghi112') : 'ghi@jbn.com',
	 }

print db[]
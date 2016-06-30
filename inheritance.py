class Person(object): #base class
	def __init__(self,name):
		self.name = name

	def showJustName(self):
		print 'My name is', self.name

class Employee(Person):  #child class, base class name is passed as arg
	def __init__(self,name,office):
		super(Employee,self).__init__(name)
		self.office = office

	def justforLaugh(self):
		print 'just for laugh'

	def showInfo(self):
		print self.name + ' ' + self.office
		super(Employee,self).showJustName()
		self.justforLaugh()

e = Employee('peter','Cluny')
e.showInfo()

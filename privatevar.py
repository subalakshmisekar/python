class Person(object):
	def __init__(self,name):
		print 'Init person'
		self.__name = name 		#private 

	def showJustName(self):
		print 'My Name is ',self.name


p = Person('suba')
p.showJustName()		#will throw error since it is accessing a private data

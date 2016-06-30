class Student(object):
	count = 0  #property of class

	def __init__(self,name):
		self.name = name
		Student.count += 1
		print name

	@staticmethod
	def showNumStudents():
		print 'Num of Students: ', Student.count


s1 = Student('abc')
s2 = Student('def')

Student.showNumStudents()


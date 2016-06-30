#Classes and Objects

class PersonalDetails(object):

	def __init__(self,name):
	    self.name = name
	    print 'Initializing Account'

p1 = PersonalDetails('Suba')
print p1.name


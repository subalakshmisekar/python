class Obj(object):
	def __init__(self,name,id):
		self.name = name
		self.id = id
		#self.eid = eid
		print name
		print id

	def __hash__(self):
		return hash((self.name,self.id)) #2braces are used since hash takes only one arg, and here we are passing it as a tuple

	def __eq__(self,x):
		return self.name == x.name and self.id == x.id

	def __repr__(self):
		return self.name + ' ' + self.id

db = { Obj('suba', 's'): 'suba@gmail.com',
       Obj('madhu', 'm'): 'madhu@gmail.com',
       Obj('uma', 'u'): 'uma@gmail.com',
     }


print db
print db[Obj('suba', 's')]
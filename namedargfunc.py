#Functions with named arguments

'''
def namedArg(name,gender):
	print 'Name: ',name,'Gender : ',gender

namedArg(gender='female',name='abc') 
'''

#unpacking functionality

db = {
	'name' : 'abc',
	'gender' : 'female',
	'location' : 'chennai',
	'age' : 20
     }

def unpackFun(name,age,gender,location):
	print name,location,age,gender

unpackFun(**db)

#order must be same while defining the list to unpack

l = ['abc',20,'male','blr']
unpackFun(*l)


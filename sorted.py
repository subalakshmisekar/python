#sorted

l = [ ['xyz',20], ['def',21], ['ijk',25] ]

def mcmp(x,y):
	print x,y
	return x[1] - y[1]

def namecmp(x,y):
	if x[0] < y[0]:
		return -1
	elif x[0] > y[0]:
		return 1
	else:
		return 0

def getkey(x):
	print 'hello'
	return x[0]

f=sorted(l,mcmp)
print f

g=sorted(l,namecmp,reverse=True)
print g

h=sorted(l,key=getkey)
print h

#functions

def myfunc(x,y):
	return x+y, x*y

msum,prod = myfunc(5,6)
print msum,prod

#tuple
m = myfunc(5,6)
print m

for d in m:
	print d

#Default arguments
def myfun(name,age,gender='male'):
	print name,age,gender

myfun('suba',24,'female')


##Variable args
def varargfun(*args):
	print args
	msum = 0
	for a in args:
		msum += a
	return msum

print varargfun(1,2,3,4,5)


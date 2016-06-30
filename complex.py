class Complex(object):
	def __init__(self,i,j):
		self.i = i
		self.j = j

	def __repr__(self):		#throws only string values. to convert the address to reqd values this is used.
		return "Complex Num: " + str(self.i) + "+" + str(self.j) + "i"

	def __add__(self,obj):
		if isinstance(obj,Complex):
			return Complex(self.i+obj.i, self.j+obj.j)
		else:
			return Complex(self.i + obj , self.j+obj)

	def __eq__(self,x):
		return self.i == x.i and self.j == x.j



num1 = Complex(2,4)
num2 = Complex(2,4)

print num1
print num2
# print num1 + num2 
# print num1 + 5

if num1 == num2:
	print 'they are same'
else:
	print 'they are not'
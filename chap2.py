#Conditional

data1 = raw_input("Enter Data1: ")
data2 = raw_input("Enter Data2: ")

if data1.isdigit() and data2.isdigit():
	print 'sum of the 2 inputs:', int(data1)+int(data2)
elif data1.isalpha() and data2.isalpha():
	print 'concatenated string: ', data1 + data2
else:
	print 'Invalid Input'


#to multiply each element in the list by 2
'''
l = [1,2,3,4,5]

for i in range(len(l)):
	l[i] *= 2

print l
'''

#global variables
football = 'None'
def play(player):
	global football   #declare in order to use inside a function
	football = player

play('abc')
play('def')
play('ghi')

print football


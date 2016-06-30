#to get input from a file, scan and put them in a dict


db = {}
for line in open('input.txt'):
	l = line.split()
	actor = l[0]
	movie = l[1]

	if actor in db:
		db[actor].append(movie)
	else:
		db[actor] = [movie]

print db
print db.items()

l = db.items()

'''
def mycmp(x,y):
	return len(x[1]) - len(y[1])

f = sorted(l, cmp = mycmp)
print f
'''

def getKey(x):
	return len(x[1])
f = sorted(l,key=getKey)
print f


'''
newdb = {}
for a,b in db.items():
	for e in b:
		if e in newdb:
			newdb[e].append(a)
		else:
			newdb[e] = [a]

print newdb 
'''

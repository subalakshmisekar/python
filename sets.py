#sets

'''
a=[]
b=[]
a = raw_input("Enter hobbies of a: ")
b = raw_input("Enter hobbies of b: ")

s1 = set(a.split())
s2 = set(b.split())

print s1
print s2
print s1 & s2
'''

def getNameHobby():
	db = {}
	while True:
		name = raw_input('Enter Name ')
		if not name:
			break

		hobbies = raw_input('Enter Hobbies ')
		hobbies = hobbies.split()
		db[name] = set(hobbies)
	return db

db = getNameHobby()

complete = []
'''
for k1 in db.keys():
	for k2 in db.keys():
		if k1 == k2:
			continue
		l = []
		l.append(k1)
		l.append(k2)
		l.append(len(db[k1] & db[k2]))
		complete.append(l)

print complete
'''

elem = db.keys()
l = list(elem)
l.sort()

res = []
for i in range(len(l)):
	for j in range(i+1,len(l)):
		x = []
		per1 = l[i]
		per2 = l[j]
		x.append(per1)
		x.append(per2)
		x.append(len(db[per1] & db[per2]))
		complete.append(x)

print type(elem)



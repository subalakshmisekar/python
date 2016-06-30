line = raw_input('Enter data: ')
l = line.split()

newl = []
for e in l:
	if not e.startswith('a'):
		newl.append(e)


print ' '.join(newl)


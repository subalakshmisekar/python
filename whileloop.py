result = 0

while True:
	data = raw_input('Enter num: ')
	if not data:
		break

	result += int(data)

print result


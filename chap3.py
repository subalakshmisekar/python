#Range

result = 0

for i in range(5):
	data = raw_input(str(i) + "Enter data: ")
	if data.isdigit():
		result += int(data)

print result


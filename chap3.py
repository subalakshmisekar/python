#Loops

# for i in range(10):
# 	print i

result = 0

for i in range(5):
	data = raw_input(str(i) + "Enter Data: ")
	if data.isdigit():
		result += int(data)

print result

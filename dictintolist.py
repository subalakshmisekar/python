#dictionary - adding dictionaries into a list and printing it


student = []
while True:
	name = raw_input("Name: ")
	if not name:
		break
	age = raw_input("Age: ")
	db = { 'name':name, 'age':age }
	student.append(db)
	

print student



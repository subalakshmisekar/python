#scanning thru entries in a dictionary

def addProductSales():
	db={}
	while True:
		product = raw_input("Enter Product ")
		if not product:
			break
		sales = int(raw_input("Sales: "))
		price = int(raw_input("Price: "))
		db[product] = {'sales':sales,'price':price}
	return db

def printReport(db):
	rev = 0
	for a,b in db.items():
		print 'Product: ',a, b['sales'],b['price']
                rev +=  b['sales']*b['price']
	print rev		

db1 = addProductSales()
printReport(db1)
#print rev


listA = []
listAsize = 0
listAvalue = 0
while  listAsize < 100:
	listAsize = listAsize + 1
	listAvalue = listAvalue + 5
	listA.append (listAvalue)

print listA

def list_reverse (listA):
	listAsize = len (listA)
	listB = []
	listBvalue = 0
	while listBvalue < listAsize:
		listB.insert (0, listA [listBvalue])
		listBvalue = listBvalue + 1
	return listB


print list_reverse (listA)

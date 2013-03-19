listA = []
listAsize = 0
listAvalue = 0
while  listAsize < 100:
	listAsize = listAsize + 1
	listAvalue = listAvalue + 5
	listA.append (listAvalue)

listB = []
listBsize = 0
listBvalue = 0
while  listBsize < 200:
	listBsize = listBsize + 1
	listBvalue = listBvalue + 2
	listB.append (listBvalue)

listC = []
listCsize = 0
indexA = 0
indexB = 0
while listCsize < (listAsize + listBsize):
	listCsize = listCsize + 1

	if indexA == listAsize:
		listC.append (listB[indexB])
		indexB = indexB + 1

	elif indexB == listBsize:
		listC.append (listA[indexA])
		indexA = indexA + 1

	elif listA[indexA] <= listB[indexB]:
		listC.append (listA[indexA])
		indexA = indexA + 1

	elif listB[indexB] < listA[indexA]:
		listC.append (listB[indexB])
		indexB = indexB + 1

print listA
print listB
print listC
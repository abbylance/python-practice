listA = [7, 7, 3, 78, 90, 4, 73, 45, 123]

def bubble_sort (listA):
	uno = 1
	while uno < len (listA):
		if (listA [uno]) >= (listA [uno - 1]):
			uno = uno + 1
		else:
			listA.insert (uno - 1, listA [uno])
			del listA [uno + 1]
			uno = 1

bubble_sort(listA)
print listA

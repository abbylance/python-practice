numbers = []
numValue = 0
while numValue < 1000:
	numbers.append(numValue)
	numValue = numValue + 1

minNum = 0
maxNum = 0
counter = 1

while maxNum < numValue:
	maxNum = minNum + counter 
	print numbers[minNum:maxNum]
	counter = counter + 1
	minNum = maxNum
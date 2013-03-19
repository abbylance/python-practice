import random 

cardValues = {
"A" : 1, 
"a" : 1,
"K" : 10,
"k" : 10,
"Q" : 10, 
"q" : 10, 
"J" : 10, 
"j" : 10, 
"10" : 10,
"9" : 9, 
"8" : 8, 
"7" : 7, 
"6" : 6, 
"5" : 5, 
"4" : 4, 
"3" : 3, 
"2" : 2
}

cardAssignment = {
14 : "A", 
13 : "K",
12 : "Q", 
11 : "J", 
10 : "10",
9 : "9", 
8 : "8", 
7 : "7", 
6 : "6", 
5 : "5", 
4 : "4", 
3 : "3", 
2 : "2"
}

def sum (cards):
	total = 0 
	for card in cards:
		total = total + cardValues[card]
	return total

print "Welcome to blackjack, whore."
print "Are you ready to lose?"

random.seed()

dealerCards = []
dcard1 = cardAssignment [random.randint(2, 14)]
dcard2 = cardAssignment [random.randint(2, 14)]
dealerCards.append (dcard1)
dealerCards.append (dcard2)

playerCards = []
card1 = cardAssignment [random.randint(2, 14)] 
card2 = cardAssignment [random.randint(2, 14)] 
playerCards.append (card1)
playerCards.append (card2)
print "Your cards are {cards}.".format(cards= ", ".join(playerCards))
print "The dealer's card is {dcard}.".format(dcard= dcard1)

dtotal = sum (dealerCards)
while dtotal < 17 :
	newCard = cardAssignment [random.randint(2, 14)]
	dealerCards.append (newCard)
	dtotal = sum (dealerCards)

answer = raw_input ("Do you want a hit? ")
while answer[0] in ["Y", "y"] :

	newCard = cardAssignment [random.randint(2, 14)]
	playerCards.append (newCard)
	print "Your cards are {cards}.".format(cards= ", ".join(playerCards))

	answer = raw_input ("Do you want a hit? ")

newTotal = sum (playerCards)
anum = playerCards.count("A")
totalList = []
totalList.append (newTotal)

while anum > 0:
	newTotal = newTotal + 10
	totalList.append (newTotal)
	anum = anum - 1

best = sum (playerCards)
for num in totalList:
	if (num <= 21) and (num > best):
		best = num

if  (dtotal < best <= 21) or (best <= 21 and dtotal > 21) :
	print "Your total is {total}. The dealer's total is {dtotal}. You win!".format(total= best, dtotal= dtotal)
elif dtotal > 21 and best > 21:
	print "Your total is {total}. The dealer's total is {dtotal}. You both lose!".format(total= best, dtotal= dtotal)
elif dtotal == best and best < 21:
	print "It's a tie! You both scored {total}".format(total= best)	
else :
	print "Your total is {total}. The dealer's total is {dtotal}. You lose, whore.".format(total= best, dtotal= dtotal)
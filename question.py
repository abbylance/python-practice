cardvalues = {
"A" : 14, 
"a" : 14,
"K" : 13,
"k" : 13,
"Q" : 12, 
"q" : 12, 
"J" : 11, 
"j" : 11, 
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
card1 = raw_input ("What is your first card?")
card2 = raw_input ("What is your second card?")
if cardvalues [card1] < cardvalues [card2] :
	print "{card2} is better than {card1}.".format(card2=card2, card1=card1)
if cardvalues [card2] < cardvalues [card1] :
	print "{card1} is better than {card2}.".format(card2=card2, card1=card1)
if cardvalues [card1] == cardvalues [card2] :
	print "Your cards are equal."
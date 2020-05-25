#Unlike a for loop. a while loop is an indefinate iteration
# loop repeats an unknown no of times till a condition is met
card_deck = [4,11,8,5,13,2,8,10]
hand=[]
while sum(hand) <= 17: #sum adds elements in a list 
    hand.append(card_deck.pop()) #pop removes the last element in a alist
print(hand)
print(card_deck)
sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

#u se a for loop to take a list and print each element of the list in its own line.
for word in sentence:
    print(word)

#   Write a for loop below that will print out every whole number that is a multiple of 5 
#   and less than or equal to 30.
for number in range(31):
    if(number>0 and number%5==0):
        print(number)

#or 
for i in range(5, 35, 5):
    print(i)
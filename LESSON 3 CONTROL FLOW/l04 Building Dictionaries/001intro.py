# create a dictionary, word_counter, that keeps track of the total count of each word in a string.
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']

# Step 1. initialize an  empty dictionary 
word_counter = {} 

# Step 2. Iterate through each element in the list
for word in book_title:
    if word not in  word_counter:
        word_counter[word] = 1
    else:
        word_counter[word]+=1

print(word_counter)

#Method 2: Using the get method
print("=== method two using GET ===")
word_counter2 = {}

for word in book_title:
    word_counter2[word] = word_counter2.get(word, 0) + 1
print(word_counter2)
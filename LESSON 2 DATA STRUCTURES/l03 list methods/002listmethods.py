#list methods
#lists are mutable 
scores = ["B","C","A","D","B","A"]
grades = scores
print("Scores : "+str(scores))
print("Grades : "+str(grades))

#now lets try and make a change on scores and see effect on grades
scores[1]="B"
print("Scores : "+str(scores))
print("Grades : "+str(grades))  #NB: grades also change with changes ade to scores

#   len()   -> returns how many elements are in a list
#   max()   -> Returns the greatest element of a list
#           -> For numbers(it returns the largest number)
#           -> for a list of strings, it's the last element if list was sorted alphabeticaly
#           -> Nb: Doesnt support a list with incomparable datatypes
#   min()   -> Returns smallest element in a list (Opposite of max)
#   sorted()-> Reurns a copy of the list sorted from smallest to largest
#           -> reverse=True   => reverses the sort order
#   join()  -> takes a list of strings as an argument, 
#              and returns a string consisting of the list elements joined by a separator string
#   append()-> Adds an ellement to the end of the list

names = ["steve", "washington","joy","peter","mary","harry"]
numbers=[23,66,12,10,99,89]

print("==========================")
print("numbers : " + str(numbers))
print("sorted : " + str(sorted(numbers)))
print("reverse : " + str(sorted(numbers,reverse=True)))

print("==========================")
print("names : " + str(names))
print("sorted: " + str(sorted(names)))
print("reverse: " + str(sorted(names, reverse=True)))

#JOIN()
sentence_names = "\n".join(names)
print(sentence_names)
#NB join() only works with strings

names.append("Hurricane")
print(names)
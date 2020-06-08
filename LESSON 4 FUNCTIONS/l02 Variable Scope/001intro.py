#  NB if a variiable is created inside 
#  a function it can only be used inside that function
# EG:
def word_count(document, search_term):
    words = document.split()
    answer = 0
    for word in words:
        if word == search_term:
            answer +=1
    return answer

def nearest_square(limit):
    answer = 0
    while(answer + 1)**2 <limit:
        answer+=1
    return answer**2

doc = "i have been here awaiting for my beloved angel,lover of my soul to  be my lifesaviour"
print(answer) # answer is not defined since it cannnot v=be accessed beyonf the functions
print(word_count(doc,'my')) #
print(nearest_square(26))
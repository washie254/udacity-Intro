"""
Iterables are objects that can return one of their elements at a time, such as a list. 
Many of the built-in functions we’ve used so far, like 'enumerate,' return an iterator.

An iterator ->  is an object that represents a stream of data. 
This is different from a list, which is also an iterable, 
but is not an iterator because it is not a stream of data.

Generators -> are a simple way to create iterators using functions. 
You can also define iterators using classes.
"""

# Example
def my_range(x):
    i = 0
    while i < x:
        yield i  #  allows function to return a value at a tiime
        i +=1 

"""
Remember, since this returns an iterator, 
we can convert it to a list or iterate through it in a loop to view its contents. 
For example, this code:
"""
for x in my_range(5):
    print(x)


"""
sq_list = [x**2 for x in range(10)]  # this produces a list of squares

sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares

"""
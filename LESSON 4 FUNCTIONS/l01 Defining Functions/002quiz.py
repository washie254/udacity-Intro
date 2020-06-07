"""
Write a function named population_density that takes two arguments, 
population and land_area, 
and returns a population density calculated from those values. 
I've included two test cases that you can use to verify that your 
function works correctly. Once you've written your function, 
use the Test Run button to test your code.
"""

# write your function here
def population_density(population,land_area):
    pop_density = population/land_area
    return pop_density

# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))

print("----------------QUIZ 2--------------\n")
"""
Write a function named readable_timedelta. 
The function should take one argument, an integer days, 
and return a string that says how many weeks and days that is. 
For example, calling the function and printing the result like this:
print(readable_timedelta(10))
1 week(s) and 3 day(s).
"""
def readable_timedelata(days):
    nweeks = int(days/7) # Or days//7
    ndays = int(days%7)
    msg = "{} weeks and {} days".format(nweeks,ndays)

    return msg

print(readable_timedelata(10))

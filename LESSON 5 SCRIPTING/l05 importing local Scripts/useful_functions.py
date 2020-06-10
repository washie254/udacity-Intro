def mean(num_list):
    return sum(num_list)/len(num_list)

def add_five(num_list):
    return [n+5 for n in num_list]

## to avoid the scripts running in other imported files  we use __main__
# this part wont run in other scriipts importing this script 
# method one :
# if __name__ == "__main__":
#     print("Testing the mean Function")
#     n_list = [34, 44, 23, 46, 12, 24]
#     correct_mean = 30.5
#     assert(mean(n_list)==correct_mean)

#     print("testing add_five function")
#     correct_list=[39, 49, 28, 51, 17, 29]
#     assert(add_five(n_list) == correct_list)

#     print("All tests passed")

# Method 2:
def main():
    print("Testing the mean Function")
    n_list = [34, 44, 23, 46, 12, 24]
    correct_mean = 30.5
    assert(mean(n_list)==correct_mean)

    print("testing add_five function")
    correct_list=[39, 49, 28, 51, 17, 29]
    assert(add_five(n_list) == correct_list)

    print("All tests passed")

if __name__ == "__main__":
    main()
points = 206  # use this input to make your submission

# write your if statement here
# 1 - 50	wooden rabbit
# 51 - 150	no prize
# 151 - 180	wafer-thin mint
# 181 - 200	penguin

if 0 < points <= 50:
    msg = "wooden rabbit"
elif points <= 150:
    msg = "no prize"
elif points <= 180:
    msg ="wafer-thin mint"
elif points <= 200:
    msg ="penguin"
else:
    print("Oh dear, no prize this time.")

result = "Congratulations! You won a {} !".format(msg)
print(result)
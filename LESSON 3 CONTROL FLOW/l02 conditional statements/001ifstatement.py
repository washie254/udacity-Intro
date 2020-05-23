# if statement runs or skips code based on whether a condition is true or false 

phone_balance = 8
bank_balance = 100

print("Current Phone Bal: {}".format(phone_balance))
print("Current Bank Bal  : {}".format(bank_balance))

if phone_balance < 5:
    phone_balance += 10
    bank_balance -=10

print("Phone Bala: {}".format(phone_balance))
print("Bank Bal  : {}".format(bank_balance))

#   Use Comparison Operators in Conditional Statements
print("------------EVEN / ODD----------")
n = 7
if n % 2==0:
    print("Number "+str(n)+" is Even")
else:
    print("Number "+str(n)+" is Odd")
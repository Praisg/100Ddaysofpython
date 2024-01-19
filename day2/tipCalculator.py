print("Welcome to the tip calculator")
bill = float(input("What is the total bill? $"))
tip = float(input("what % tip would you like to give?"))
people = float(input("How many people to split the bill? "))

amount = (bill*(1+(tip/100)))/people

print("Each person should pay: ${:.2f}".format(amount))
#
print("Welcome to my Python Pizza Deliveries\n We have Small($15), Medium($20) and Large($25) Pizzas")
size = input("what size do you want? S, M or L\n")
add_pepperoni = input("Do you want pepperoni ($2 for small and $3 for other sizes)? Y or N\n")
extra_cheese = input("Do you want extra cheese for a $1? Y or N\n")
#if someone wants 2 types or all, i will revist this and try to make the string inputs separate like SML to be S M L 
bill = 0
if size== "S":
    bill= 15
    if add_pepperoni== "Y":
        bill +=2
    if extra_cheese=="Y":
        bill +=1
elif size=="M":
    bill= 20
    if add_pepperoni=="Y":
        bill +=3
    if extra_cheese=="Y":
        bill +=1   
elif size=="L":
    bill= 25
    if add_pepperoni=="Y":
        bill +=3
    if extra_cheese=="Y":
        bill +=1   
print(f"Your final bill is ${bill}")                    

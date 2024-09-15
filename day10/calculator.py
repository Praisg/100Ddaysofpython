from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subt(n1, n2):
    return n1-n2

def mult(n1, n2):
    return n1*n2

def div(n1, n2):
    if n1 == 0 or n2 == 0:
        return "Divisible by zero error"
    else:
         return n1/n2
    
to_continue = True
while to_continue == True:

    Operat = { "+":add,
                "-":subt, 
                "*":mult, 
                "/":div 
                }

    num1 =float(input("Enter your first number\n"))
    num2 =float(input("Enter your second number\n"))

    for symbol in Operat:
        print(symbol)
    result= input("Choose Operation\n")

    first_answer= Operat[result](num1,num2)#im proud of myself, This takes the operator(result) and call the value in dictionary(Operat) , offwhich that value is the function 
    print(f"{num1} {result} {num2} = {first_answer}")
    
    userr = input("Type Y to continue or N to Exit\n").lower()
    if userr == "n":
        to_continue = False
    else:
        print(logo)    
        result= input("Choose another Operation\n")
        num3 = float(input("Whats the next number\n"))
        second_answer = Operat[result](Operat[result](num1,num2), num3)
        print(f"{first_answer} {result} {num3} = {second_answer}")
    
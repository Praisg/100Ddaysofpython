from coffee import MENU, resources

cash = 0 #made global 

def machin(coff):
    for item in MENU[coff]["ingredients"]: #item is the key
        if item in resources:
            if resources[item] < MENU[coff]["ingredients"][item]:
                print(f"There is not enough {item} ")
                return False #so that we stop 
            else:
                resources[item] -= MENU[coff]["ingredients"][item]
            
    return resources
    
def coins (coff):
    global cash #made global so that i can assess it in the if statement below
    print("Please insert coins")
    quarters = float(input("How many quarters?: ")) * 0.25
    dimes = float(input("How many dimes?: ")) * 0.1
    nickles = float(input("How many nickles?: ")) * 0.05
    pennies = float(input("How many pennies?: ")) * 0.01
    money = quarters + dimes + nickles + pennies 
    change = money - MENU[coff]["cost"] 
    
    if change> 0:
        print("Here is ${:.2f}".format(change),'in change')
        print(f"Here is your {coff}, enjoy")
        cash += money - change
    else:
        print("Sorry thats not enough money. Money refunded")   

prompt = True
while prompt:
    coff= input("What would you like? (espresso/latte/cappuccino):")
   
    if coff== 'off':
        prompt= False
    elif coff =="report":
            print(resources)
            print(f"Money: {round(cash, 2)}")
    else:
        if machin(coff):# if false from machin() we wont ask for coins 
            coins(coff)
        
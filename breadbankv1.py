from random import randint

bread_bank_balance = 100
print(f"You have a starting balance of {bread_bank_balance} pieces of bread in your Bread Bank")
bread = "🍞"
x=int(input("How many pieces of bread would you like from the bread bank? "))
interest_rate= float(0.10)

while x>bread_bank_balance:
    print("You don't have enough bread in your bread bank.")
    y=input("Would you like to borrow bread from the Big Bread Bank? ")
    if y== "yes":
        z=int(input("How many pieces of bread would you like to borrow? "))
        print (f"You've borrowed {z} pieces of bread.")
        print(f"There will be charge of 10% monthly interest for any \nunpaid balance of the {z} pieces of bread you've borrowed. ")
        ex_numb=randint(1,z)
        print(f"For example, if you've paid back {ex_numb} pieces of the bread you owe on this \nmonth, you'd now owe {round(z-ex_numb)*(1.0+interest_rate)} pieces of bread on your payment next month.")
        break
    
else: 
    print(x*bread + "\nHere are the pieces of bread you've requested.")
    print (f"You now have have {bread_bank_balance-x} pieces of bread left in your bread bank.")

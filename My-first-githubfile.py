print("welcome to state bank ")
print("Insert the atm card")
yes = input()
if yes == "y":
    print("Enter 4 digit pin")
else :
    print("Card not inserted please check again")
    pin1 = int(input())
    pin = 1234
if  pin == pin1:
        language = int(input("enter your preferred language 1.English 2.Kannada 3.Telugu:"))
else:
    print("Incorrect pin")
if language == 1 :
        print("your prefered language is 1")
else:
        print("your prefered language is kannada")
    Bal = int(input("select options 1.Withdraw 2.deposit:"))
    w = 10000
    print(f"Balance :{w}")
if bal == 1:
        a = int(input("Enter withdraw amount:"))
 if a>w :
            print(f"Now your available balance is :{w+b}")
            print("processing.....")
            print("Please collect the cash")
            print("Thank you")
            print("Visit again1")
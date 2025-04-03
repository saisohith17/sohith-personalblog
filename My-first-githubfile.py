print("Welcome to State Bank")
print("Insert the ATM card (y/n):")
yes = input().strip().lower()  # Converts input to lowercase and removes spaces

if yes == "y":
    pin1 = int(input("Enter 4-digit PIN: "))
    pin = 1234

    if pin == pin1:
        language = int(input("Enter your preferred language: \n1. English \n2. Kannada \n3. Telugu\n"))

        if language == 1:
            print("Your preferred language is English")
        else:
            print("Your preferred language is Kannada")

        bal = int(input("Select options: \n1. Withdraw \n2. Deposit\n"))
        w = 10000  # Initial balance
        print(f"Your Balance: {w}")

        if bal == 1:
            a = int(input("Enter withdraw amount: "))

            if a > w:
                print("Insufficient Balance!")
            else:
                w -= a  # Deducting the withdrawal amount
                print(f"Now your available balance is: {w}")
                print("Processing.....")
                print("Please collect the cash")
                print("Thank you")
                print("Visit again")

        elif bal == 2:
            d = int(input("Enter deposit amount: "))
            w += d  # Adding deposit amount
            print(f"Now your available balance is: {w}")
            print("Deposit successful!")

        else:
            print("Invalid option selected")

    else:
        print("Incorrect PIN! Try again.")

else:
    print("Card not inserted. Please check again.")

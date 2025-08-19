# Show a welcome message
print("Welcome to MEST ATM")
print("Please Insert your Card>>> ")

# Ask the user to insert the card 4-last digits
user_card_name = input("Enter your name:\n")
user_card_number = int(input("Enter your serial number>> ")) 

# Ask user to enter their pin
user_pin = 4190
# Current balance
current_balance = 10000.00


def pin_authenticate():
    while True:
        pin = int(input("Enter your pin>> "))
        try:
            if pin == user_pin:
                print("Login Successful")
                break
            else:
                print("Authentication failed")
        except ValueError:
            print("Invalid pin - Try again!")
    return pin
pin_authenticate()

def withdrawal():
    global current_balance
    amount = float(input("Enter the amount>>\n "))
    if amount <= 0:
        print("Invalid input")
        return 
    if amount <= current_balance:
 # storing the current balance after deductions
        current_balance -= amount
        print("Withdrawal Successful,Please take your card.")
    else:
        print("Insufficient balance")

# Display options
def choices():
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Transaction History")
    print("5. Exit")

    options = input("Choose an option>>\n ")
    if options == "1":
        print(f"Your current balance is GHC {current_balance}")
    elif options == "2":
        print("Ready to deposit")
    elif options == "3":
        withdrawal()
    elif options == "4":
        print("History")
    elif options == "5":
        print("Exit")
    else:
        print("Choose from the options")
choices()
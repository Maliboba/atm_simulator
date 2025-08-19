import datetime
# The user's PIN is a fixed value 
user_pin = 4190
# Variables 
current_balance = 10000.00
transaction_history = []
daily_withdrawal_limit = 5000
total_withdrawn_today = 0

# Welcome and User Authentication 
print("Welcome to MEST ATM")
print("Please Insert your Card>>> ")

user_card_name = input("Enter your name:\n")

def pin_authenticate():
    """Authenticates the user's PIN with a limited number of tries."""
    tries = 0
    while tries < 3:
        try:
            pin = int(input("Enter your pin>> "))
            if pin == user_pin:
                print("Login Successful")
                return True
            else:
                print("Authentication failed. Try again.")
                tries += 1
        except ValueError:
            print("Invalid PIN - Please enter a number.")
            tries += 1
    print("Too many failed attempts. Your card has been blocked.")
    return False

#  Helper Functions 
def show_menu():
    """Displays the main menu options to the user."""
    print("\n--- ATM Main Menu ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Exit")
    print("---------------------")

def generate_receipt(transaction_type, amount):
    """Prints a formatted receipt for a given transaction."""
    global current_balance
    print("\n--------------------------")
    print("      ATM RECEIPT")
    print(f"Transaction: {transaction_type}")
    print(f"Amount: GHC {amount:.2f}")
    print(f"Balance: GHC {current_balance:.2f}")
    print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("--------------------------\n")

def view_transaction_history():
    """Displays a list of all transactions made."""
    if not transaction_history:
        print("No transactions to display.")
    else:
        print("\n--- Transaction History ---")
        for transaction in transaction_history:
            print(f"Type: {transaction['type']}")
            print(f"Amount: GHC {transaction['amount']:.2f}")
            print(f"Balance: GHC {transaction['balance']:.2f}")
            print(f"Date: {transaction['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")
            print("-------------------------")

# Core Functionalities 
def check_balance():
    """Displays the user's current balance."""
    print(f"Your current balance is GHC {current_balance:.2f}")

def deposit():
    """Allows the user to deposit money into their account."""
    global current_balance
    global transaction_history
    
    try:
        amount = float(input("Enter amount to deposit: GHC "))
        if amount <= 0:
            print("Invalid amount. Please enter a positive value.")
        else:
            current_balance += amount
            print("Deposit successful.")
            
            # Record the transaction
            transaction_history.append({
                "type": "Deposit",
                "amount": amount,
                "balance": current_balance,
                "timestamp": datetime.datetime.now()
            })
            generate_receipt("Deposit", amount)
    except ValueError:
        print("Invalid input. Please enter a number.")

def withdrawal():
    """Allows the user to withdraw money from their account."""
    global current_balance
    global total_withdrawn_today
    global transaction_history
    
    try:
        amount = float(input("Enter amount to withdraw: GHC "))
        if amount <= 0:
            print("Invalid amount. Please enter a positive value.")
        elif amount > current_balance:
            print("Insufficient balance.")
        elif (total_withdrawn_today + amount) > daily_withdrawal_limit:
            print(f"Daily withdrawal limit of GHC {daily_withdrawal_limit:.2f} exceeded.")
        else:
            current_balance -= amount
            total_withdrawn_today += amount
            print("Withdrawal successful. Please take your cash.")
            
            # Record the transaction
            transaction_history.append({
                "type": "Withdrawal",
                "amount": amount,
                "balance": current_balance,
                "timestamp": datetime.datetime.now()
            })
            generate_receipt("Withdrawal", amount)
    except ValueError:
        print("Invalid input. Please enter a number.")

#  Main Program Logic 
if pin_authenticate():
    while True:
        show_menu()
        option = input("Choose an option: ")
        
        if option == '1':
            check_balance()
        elif option == '2':
            deposit()
        elif option == '3':
            withdrawal()
        elif option == '4':
            view_transaction_history()
        elif option == '5':
            print("Thank you for using our ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please choose from 1 to 5.")
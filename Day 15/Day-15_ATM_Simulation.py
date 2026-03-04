while True:
    print("\n---ATM Simulation Menu---")
    print("1. Check average transaction (ZeroDivisionError)")
    print("2. Withdraw with Invalid input(ValueError)")
    print("3. Deposit with invalid data type(TypeErrror)")
    print("4. Acess Invalid Transcation History(IndexError)")
    print("5. Acess Non-Existent Account(KeyError)")
    print("6. Read Missing Transaction Log File(FileNotFoundError)")
    print("7. Exit")

    choice = input("select an option(1-7): ")

    if choice == "1":
        zero_division_error_case()
    elif choice == "2":
        value_error_case()
    elif choice == "3":
        type_error_case()
    elif choice == "4":
        index_error_case()
    elif choice == "5":
        key_error_case()
    elif choice == "6":
        file_not_found_error_case()
    elif choice == "7":
        print("Exiting the ATM simulation. Goodbye")
        break
    else:
        print("wrong Choise")
def zero_division_error_case():
    try:
        transactions = []
        average_transaction = sum(transactions) / len(transactions)
        print("Average Transaction: ",average_transaction)
    except ZeroDivisionError:
        print("Error: Cannot caluclate abverage transaction because there are no values")

def value_error_case():
    try:
        withdrawl_amount = int("100/")
        print("withdrawing: ",withdrawl_amount)
    except ValueError:
        print("Error: Invalid value entered. Please enter a numerical amount.")

def type_error_case():
    try:
        balance = 500
        deposit_amount = '100'
        new_balance = balance + deposit_amount
        print("New Balance= ",new_balance)
    except TypeError:
        print("Error: Incomplitable data type cannot add string to an integer")

def index_errror_case():
    try:
        transaction_history = [200, -100, 300]
        print("Last Transaction: ",transaction_history[5])
    except IndexError:
        print("Error: Trying to access a transaction that does not exist.")
def key_error_case():
    try:
        accounts = {}

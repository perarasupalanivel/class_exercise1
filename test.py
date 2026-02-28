user_name = "JohnDoe"
account_balance = 1000.0


def check_balance():
    print(f"Hello, {user_name}! Your current balance is: ${account_balance:.2f}")


def deposit():
    global account_balance
    amount = float(input("Enter amount to deposit: $"))
    if amount > 0:
            account_balance += amount
            print(f"Successfully deposited ${amount:.2f}.")
            check_balance()
    else:
            print("Deposit amount must be positive.")




def withdraw():
    global account_balance # Declare as global to modify the variable outside the function
    amount = float(input("Enter amount to withdraw: $"))
    if amount > 0:
            if account_balance >= amount:
                account_balance -= amount
                print(f"Successfully withdrew ${amount:.2f}.")
                check_balance()
            else:
                print("Insufficient funds.")





def main():
 print("Welcome to the Simple Banking System!")
while True:
        print("\n--- Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            check_balance()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            print("Thank you for using our banking system. Goodbye")

main()

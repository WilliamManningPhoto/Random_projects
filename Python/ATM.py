
def ATM():
    print("Welcome to the ATM!")
    balance = 1000  # Initial balance

    while True:
        print("\nSelect an option:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print(f"Your current balance is: ${balance:.2f}")
        elif choice == '2':
            amount = float(input("Enter amount to deposit: $"))
            if amount > 0:
                balance += amount
                print(f"${amount:.2f} deposited successfully.")
            else:
                print("Invalid amount. Please enter a positive number.")
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: $"))
            if 0 < amount <= balance:
                balance -= amount
                print(f"${amount:.2f} withdrawn successfully.")
            else:
                print("Invalid amount. Please enter a positive number within your balance.")
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

ATM()
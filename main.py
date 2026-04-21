from bank import BankAccount

def main():
    # create empty accounts list
    accounts = []
    
    # start main loop
    while True:
    
        # display menu options
        print("\n----- Bank CLI -----")
        print(" 1. Create a New Account")
        print(" 2. Make a Deposit")
        print(" 3. Make a Withdrawal")
        print(" 4. Make a Transfer")
        print(" 5. Show Account Transaction History")
        print(" 6. List all Accounts")
        print(" 7. Quit")
        
        # get user input
        choice = input("Choice: ").strip()
        
        # if create account
        if choice == "1":
            # get owner name and balance
            owner = str(input("Account Owner Name: ".strip()))
            try:
                balance = float(input("Account Balance: "))
            # create BankAccount instance
                acc = BankAccount(owner,balance)
            # append to accounts list
                accounts.append(acc)
                print(f"Created: {acc}")
            except ValueError as e:
                print(f"Error: {e}")
        
        # if deposit/withdraw/transfer/history
        elif choice in ("2", "3", "4", "5"):
            # check if accounts exist
            # select account
            # perform action
            continue
        
        elif choice == "6":
            continue

        # if quit
        elif choice == "7":
            # exit loop
            print("Goodbye")
            break

        else:
            print("Invalid selection. Please choose 1-7")

if __name__ == "__main":
    main()
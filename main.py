from bank import BankAccount


def select_account(accounts):
    for i, acc in enumerate(accounts):
        print(f" {f'{i + 1}. {acc.owner}':<20} ${acc.balance:.2f}")
    try:
        index = int(input("Select account (number): ").strip()) - 1
        if 0 <= index < len(accounts):
            return accounts[index]
        print("Invalid selection.")
    except ValueError:
        print("Please enter an integer.")
    return None


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
            if not accounts:
                print("No accounts exist yet.")
                continue
            # select account
            acc = select_account(accounts)
            if acc is None:
                continue

            # perform action

            #deposit
            if choice == "2":
                try:
                    amount = float(input("Amount to deposit: $").strip())
                    acc.deposit(amount)
                    print(f"New Balance: ${acc.balance:.2f}")
                except ValueError as e:
                    print(f"Error: {e}")
            
            #withdraw
            elif choice == "3":
                try:
                    amount = float(input("Amount to withdrawal: $").strip())
                    acc.withdraw(amount)
                    print(f"New Balance: ${acc.balance:.2f}")
                except ValueError as e:
                    print(f"Error: {e}")

            #transfer
            elif choice == "4":
                if len(accounts) < 2:
                    print("Need at least 2 accounts for a transfer.")
                    continue
                print("Transfer to: ")
                targets = [a for a in accounts if a is not acc]
                target = select_account(targets)
                if target is None:
                    continue
                try:
                    amount = float(input("Amount to transfer: $").strip())
                    acc.transfer(amount,target)
                    print(f"You transferred ${amount:.2f} to {target.owner}. Your balance is now ${acc.balance:.2f}")
                except ValueError as e:
                    print(f"Error: {e}")

            elif choice == "5":
                history = acc.get_history()
                if not history:
                    print("There are no transactions yet.")
                else:
                    for transaction in history:
                        print(f" {transaction['type']:<20} ${transaction['amount']:.2f}")
        
        elif choice == "6":
            if not accounts:
                print("No accounts exist yet.")
            else:
                for i, acc in enumerate(accounts):
                    print(f" {f'{i + 1}. {acc.owner}':<20} ${acc.balance:.2f}")

        # if quit
        elif choice == "7":
            # exit loop
            print("Goodbye")
            break

        else:
            print("Invalid selection. Please choose 1-7")

if __name__ == "__main":
    main()
from bank import BankAccount
import json


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


def save(accounts):
    save_state = [{"owner": acc.owner, "balance": acc.balance, "transactions": acc.transactions} for acc in accounts]
    with open("save_state.json", "w") as f:
        json.dump(save_state, f, indent=2)


def load():
    accounts = []
    try:
        with open("save_state.json", "r") as f:
            load_state = json.load(f)
    except FileNotFoundError:
        return []
    if not load_state:
        return []
    else:
        return [BankAccount(item['owner'], item['balance'], item['transactions']) for item in load_state]       


def main():
    accounts = load()
    
    while True:
        print("\n----- Bank CLI -----")
        print(" 1. Create a New Account")
        print(" 2. Make a Deposit")
        print(" 3. Make a Withdrawal")
        print(" 4. Make a Transfer")
        print(" 5. Show Account Transaction History")
        print(" 6. List all Accounts")
        print(" 7. Quit")
        
        choice = input("Choice: ").strip()
        
        if choice == "1":
            owner = input("Account Owner Name: ").strip()
            try:
                balance = float(input("Account Balance: "))
                acc = BankAccount(owner,balance)
                accounts.append(acc)
                print(f"Created: {acc}")
                save(accounts)
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice in ("2", "3", "4", "5"):
            if not accounts:
                print("No accounts exist yet.")
                continue
            acc = select_account(accounts)
            if acc is None:
                continue

            if choice == "2":
                try:
                    amount = float(input("Amount to deposit: $").strip())
                    acc.deposit(amount)
                    print(f"New Balance: ${acc.balance:.2f}")
                    save(accounts)
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif choice == "3":
                try:
                    amount = float(input("Amount to withdrawal: $").strip())
                    acc.withdraw(amount)
                    print(f"New Balance: ${acc.balance:.2f}")
                    save(accounts)
                except ValueError as e:
                    print(f"Error: {e}")

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
                    save(accounts)
                except ValueError as e:
                    print(f"Error: {e}")

            elif choice == "5":
                history = acc.get_history()
                if not history:
                    print("There are no transactions yet.")
                else:
                    for transaction in history:
                        print(f" {transaction['type']:<20} {transaction['to']:<20} {transaction['from']:<20} ${transaction['amount']:>20.2f}")
        
        elif choice == "6":
            if not accounts:
                print("No accounts exist yet.")
            else:
                for i, acc in enumerate(accounts):
                    print(f" {f'{i + 1}. {acc.owner}':<20} ${acc.balance:.2f}")

        elif choice == "7":
            print("Goodbye")
            break

        else:
            print("Invalid selection. Please choose 1-7")


if __name__ == "__main__":
    main()
# Simple Bank CLI
> Managing multiple bank accounts with persistent state. For educational purposes only.

## What it does
A command-line banking application that lets users create and manage multiple accounts with deposits, withdrawals, and transfers. Account state persists between sessions via a local JSON save file — useful as a foundation for any application requiring stateful object management.

## Features
- CLI user-interface
- Account state persists across sessions

## Setup
1. Clone the repository
2. Install Python 3.12

## Run
```
python bank_cli.py
```

## Example Output

```
----- Bank CLI -----
 1. Create a New Account
 2. Make a Deposit
 3. Make a Withdrawal
 4. Make a Transfer
 5. Show Account Transaction History
 6. List all Accounts
 7. Quit
Choice: 

Choice: 1
Account Owner Name: account_owner_1
Account Balance: $100.00
Created: The bank account for account_owner_1 has a balance of $100.00

Choice: 5
 1. account_owner_1 $150.00
 2. account_owner_2 $150.00
Select account (number): 1
 type                 to                   from                          amount
 starting balance                                               $        100.00
 deposit              account_owner_1                           $        200.00
 withdrawal                                account_owner_1      $       -100.00
 transfer             account_owner_2      account_owner_1      $       -100.00
 transfer             account_owner_1      account_owner_2      $         50.00
```

## What I learned
Building this project solidified OOP fundamentals, specifically how encapsulation keeps validation logic inside the class itself so bad data can never get through regardless of how the class is used. Implementing save and load functionality added practical experience with serializing and deserializing custom objects to JSON for persistent state.
# Bank Account

> A Python CLI application for managing multiple bank accounts with deposit, withdrawal, transfer, and transaction history capabilities.

## What it does
Implements a `BankAccount` class and an interactive CLI that allows users to create and manage multiple bank accounts. Demonstrates OOP fundamentals including encapsulation, instance methods, and error handling.

## Inputs
- Owner name (string) provided at account creation
- Initial balance (float) provided at account creation
- Transaction amounts (float) passed to deposit, withdraw, and transfer methods
- Target account selection for transfers
- Menu selections (integer) for navigating the CLI

## Outputs
- Updated account balance after each transaction
- Transaction history list via `get_history()`
- Human-readable account summary via `__str__`
- Unambiguous developer representation via `__repr__`
- Interactive CLI menu for creating accounts and performing operations

## Success criteria
- Any number of accounts can be created at runtime
- All methods raise descriptive `ValueError` on invalid input
- Withdrawals and transfers rejected when amount exceeds balance
- Transfers correctly debit source and credit target account
- Transaction history accurately reflects all operations in order
- CLI handles invalid menu selections gracefully without crashing
- Both `__str__` and `__repr__` implemented and tested in the REPL
- No external API keys or secrets required
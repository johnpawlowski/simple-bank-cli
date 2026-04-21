class BankAccount:
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def __repr__(self):
        pass
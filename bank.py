class BankAccount:
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}(owner={self.owner}, balance={self.balance})"
    
    def __str__(self):
        pass
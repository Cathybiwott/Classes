
# Add attributes deposits and withdrawals in the init method which are empty lists by default and another attribute loan_balance which is zero by default.

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0
# Add a method check_balance which returns the account’s balance
    
    def check_balance(self):
        return self.balance

# Update the deposit method to append each withdrawal transaction to the deposits list. Each transaction should be in form of a dictionary like this  
# {
#    "amount": amount,
#    "narration": “deposit”
# }
    
    def deposit(self, amount):
        self.balance += amount
        self.deposits.append(amount)
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.withdrawals.append(amount)
            return True
        else:
            return False

# Update the withdrawal method to append each withdrawal transaction to the withdrawals list. Each transaction should be in form of a dictionary like like this 
# {
#    "amount": amount,
#    "narration": “withdrawal”
# }
    
    def print_statement(self):
        for deposit in self.deposits:
            print(f"deposit - {deposit}")
        for withdrawal in self.withdrawals:
            print(f"withdrawal - {withdrawal}")

# Add a borrow_loan method which allows a customer to borrow if they meet these conditions:
# Account has no outstanding loan
# Loan amount requested is more than 100
# Customer has made at least 10 deposits.
# Amount requested is less than or equal to 1/3 of their total sum of all deposits.
# A successful loan increases the loan_balance by requested amount
    
    def borrow_loan(self, amount):
        if self.loan_balance == 0 and amount > 100 and len(self.deposits) >= 10 and amount <= (sum(self.deposits)/3):
            self.loan_balance += amount
            self.balance += amount
            return f"Loan of {amount} taken successfully"
        else:
            return "Loan unsuccessful"

# Add a repay_loan method with this functionality
# A customer can repay a loan to reduce the current loan_balance
# Overpayment of a loan increases the accounts current balance
 
    
    def repay_loan(self, amount):
        if amount <= self.loan_balance:
            self.balance -= amount
            self.loan_balance -= amount
        else:
            self.balance -= self.loan_balance
            self.deposit(amount - self.loan_balance)
            self.loan_balance = 0

# Add a transfer method which accepts two attributes (amount and instance of another account). If the amount is less than the current instances balance, the method transfers the requested amount from the current account to the passed account. The transfer is accomplished by reducing the current account balance and depositing the requested amount to the passed account.

    def transfer(self, amount, receiver):
        if self.balance >= amount:
            self.balance -= amount
            receiver.balance += amount
            return "Transfer successful"
        else:
            return "Transfer unsuccessful"


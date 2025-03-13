class BankAccount:
    def __init__(self, account_number):
       
        self.account_number = account_number  
        self.balance = 0  

    def deposit(self, amount):
       
        if amount > 0:  
            self.balance = self.balance + amount  
            print("Deposited:", amount)
            print("New balance:", self.balance)
        else:
            print("Amount must be positive")

    def withdraw(self, amount):
        
        if amount > 0: 
            if amount <= self.balance:  
                self.balance = self.balance - amount 
                print("Withdrew:", amount)
                print("New balance:", self.balance)
            else:
                print("Not enough money in the account")
        else:
            print("Amount must be positive")

    def get_balance(self):

        return self.balance 



account = BankAccount("12345")


print("Account Number:", account.account_number)
print("Starting balance:", account.get_balance())  

account.deposit(100)  
account.withdraw(50)  

print("Final balance:", account.get_balance())  
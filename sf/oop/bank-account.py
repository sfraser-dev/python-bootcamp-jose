class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def __str__(self):   # run this when "print(class) is called"
        return (f"account holder is {self.owner}")
        
    def deposit(self, x):
        self.depsit = x
        print('deposit accepted')

    def withdraw(self, x):
        if x > self.balance:
            print('cannot withdraw more than you have in the account')
        else:
            self.balance -= x
            print('withdrawal accepted')

acct1 = Account('Jose',100)
acct1.withdraw(200)
# 1. Instantiate the class
acct1 = Account('Jose',100)
# 2. Print the object
print(acct1)
# 3. Show the account owner attribute
acct1.owner
# 4. Show the account balance attribute
acct1.balance
# 5. Make a series of deposits and withdrawals
acct1.deposit(50)
acct1.withdraw(75)
# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)
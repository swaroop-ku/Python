class bank:
    def __init__(self):
        self.total = int(input("Enter the total balance in your account:"))

    def tbalance(self):
        print("Total balance:",self.total)

class myaccount(bank):
    def action(self):
        self.withdraw = int(input("Enter the amount you want to withdraw:"))
        if self.withdraw > self.total :
            print("Insufficient funds")
        else:
            print("Amount withdrawl successfully")
            self.total = self.total - self.withdraw

obj = myaccount()
obj.action()
obj.tbalance()
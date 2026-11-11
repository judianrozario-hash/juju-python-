class Bank:
     def __init__(self,acc_no,name,acc_type,balance):
         self.acc_no=acc_no
         self.name=name
         self.acc_type=acc_type
         self.balance=balance
     def deposit(self,amount):
           self.balance=self.balance+amount
           print("Amount deposited successfully")
     def withdraw(self,amount):
            if amount<=self.balance:
                self.balance=self.balance-amount
                print("Amount withdraw successfully")     
            else:
               print("insufficient balance")
     def display(self):
           print("Account number:",self.acc_no)
           print("name:",self.name)
           print("Account type:",self.acc_type)
           print("Balance:",self.balance)
b1=Bank(101,"anu","savings",5000)
b1.display()
b1.deposit(2000)
print("Balance after deposit:",b1.balance)
b1.withdraw(1000)
print("Balance after withdrawal:",b1.balance)

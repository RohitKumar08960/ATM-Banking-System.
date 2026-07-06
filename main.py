# ATM BANKING SYSTEM

class BankAccount:
    def __init__(self, name, account_number, pin, balance=0):
        self.name = name
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

# verify pin

    def verify_pin(self):
        entered_pin = input("enter 4 digit pin : ")
        if entered_pin == self.pin:
             print("login successfull")
             return True
        else:
            return False
    
# deposit money

    def deposit_amount(self):
        amount = float(input ("enter deposit amount: "))
    
        if amount >0:
           self.balance += amount
           self.transaction_history.append("amount")
           print("amount successfully deposit")
    
        else:
         print("invalid amount")
         
# withdraw Money

    def withdraw(self):
        amount = float(input("enter withdraw amount: "))
    
        if amount <=0:
          print("invalid amount")
        
        elif  amount > self.balance:
          print("insefficiant balance")
        
        else:
          self.balance -= amount
          self.transaction_history.append("amount withdraw")
          print("amount withdraw successfully")
        
    def check_balance(self):
        print("current balance:", self.balance)
        
    def menu(self):
        while True:
              print("=====ATM menu=====")
              print("1.deposit")
              print("2.withdraw")
              print("3.checkbalance")
              print("4.exit")
        
              choise = input("enter the choise: ")
        
              if choise == "1":
                 self.deposit_amount()
    
              elif choise == "2":
                self.withdraw()
    
              elif choise == "3":
                self.check_balance()   
    
              elif choise == "4":
                print("thanking you for visitint ATM.")
                break

              else:
                 print("invalid choise, try again ")
    
    
    
account = BankAccount(
    name ="Rohit",
    account_number="0987654321",
    pin="6243",
    balance=8284
)

print("Welcome to ATM Banking System")

if account.verify_pin():
    account.menu()


            
            
        
        
    
    
    
    
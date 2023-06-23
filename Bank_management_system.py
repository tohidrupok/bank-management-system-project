class User:
    def __init__(self,username,password) -> None:
        self.username = username
        self.password = password

class History:
    def __init__(self, name, amount, widthraw = 0, diposit = 0, transfer = 0,lone = 0) -> None:
        self.name = name
        self.amount = amount
        self.widthraw = widthraw
        self.diposit = diposit
        self.transfer = transfer
        self.lone = lone

class Grahok(User):
    def __init__(self, username, password,bank) -> None:
        super().__init__(username, password)
        self.balance = 0
        self.bank = bank
        
        self.history = []

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            self.bank.total_balance += amount
            history = History(self.username, self.check_balance(), 0, amount,0, 0)
            self.history.append(history)

    def withdrawa(self,amonunt):
        if self.balance > amonunt:
            self.balance -= amonunt
            self.bank.total_balance -= amonunt
            history = History(self.username, self.check_balance(), amonunt, 0,0,0)
            self.history.append(history) 
            return True
        else:
            return False

    def check_balance(self):
        return self.balance
    
    def take_lone(self,amount):
        capacity = self.balance*2
        if capacity > amount:
            self.balance+= amount
            self.bank.total_balance -= amount
            self.bank.total_loan += amount
            history = History(self.username, self.check_balance(), 0, 0,0,amount)
            self.history.append(history) 
            print('Loan Done and amount is: ',amount)
        else:
            print('not enouth your money.')
    def  transfer_amount(self,other_user,amount):
        if self.balance >= amount:
            self.balance -= amount
            other_user.deposit(amount)
            history = History(self.username, self.check_balance(), 0,0, amount, 0)
            self.history.append(history) 
            return True
        else:
            return False
    def history_transaction(self):
        Day = 0
        for report in self.history:
            Day+=1
            print(f"\n {' ' * 10}")
            print(f'User Name: {report.name}, Day:{Day}----> amoutn: {report.amount} Day:{Day}----> withdraw: {report.widthraw} Day:{Day}----> diposit: {report.diposit} Day:{Day}----> transfer: {report.transfer} Day:{Day}----> lone:{report.lone}')


class Bank:
    def __init__(self,name) -> None:
        self.name = name 
        self.total_balance = 1000
        self.total_loan = 0
        self.loan_system = True

    def check_total_balance(self):
        return self.total_balance
    def check_total_loan(self):
        return self.total_loan 
    def on_loan_system(self):
        self.loan_system = True
    def off_loan_system(self):
        self.loan_system = False
    
class admin(User):
    def __init__(self, username, password) -> None:
        super().__init__(username, password)
    def __init__(self, username, password):
        super().__init__(username, password)

    def check_total_balance(self, bank):
        return bank.check_total_balance()

    def check_total_loan(self, bank):
        return bank.check_total_loan()

    def enable_loan_feature(self, bank):
        bank.on_loan_system()

    def disable_loan_feature(self, bank):
        bank.off_loan_system()    
    
class system(Grahok):
    def __init__(self):
        self.user_list = []
        self.admin_list = []
        self.bank = Bank("MyBank")

    def create_account(self):
        print('\n1.Admin Create Account\n2.Grahok Create Account')
        a = int(input('Enter Your option: '))
        if a == 2:

            name = input("Enter User(YOU) Username : ")
            password = input("Enter a password : ")
            self.new_account = Grahok(name, password,self.bank)

            self.user_list.append(self.new_account)
            print('\t\tCongratulations.Now you are our new genaral member.')
        elif a==1:
            name = input("Enter Admin sir Username : ")
            password = input("Enter a password : ")
            self.admin_account = admin(name, password)

            self.admin_list.append(self.admin_account)
            print('\t\tCongratulations Admin Sir.Now you are our new Admin.')
            
    def admin_menu(self, admin):
        while True:
            print(f"\n {' ' * 10}Welcome back admin sir in Banking Management System.")
            print("1.total available balance\n2.total loan amount\n3.on the loan Sytem\n4.OFF the loan sytem.\n5.EXIT")

            choice = input("Enter Your Choice: ")
            if choice == "5":
                break
            elif choice == "1":
                total_balance = admin.check_total_balance(self.bank)
                print("\t\tTotal Available Balance:", total_balance)
            elif choice == "2":
                total_loan = admin.check_total_loan(self.bank)
                print("\t\tTotal Loan Amount:", total_loan)
            elif choice == "3":             
                admin.enable_loan_feature(self.bank)
                print("\t\tLoan system on.")
            elif choice == "4":           
                admin.disable_loan_feature(self.bank)
                print("\t\tLoan system off.")   
    def user_menu(self, user):
        
        while True:
            print(f"\n {' ' * 10}Welcome to Banking Management System.")
            print("\n1.Check Available Balance\n2.Deposit amount \n3.Withdrawal Amount\n4.Transfer The Amount\n5.Check Transaction History.\n6.Take a Loan\n7.Exit") 

            a = input("Enter Your option: ")
            if a == "7":
                break
            elif a == "1":
                balance = user.check_balance()
                print("\t\tAvailable Balance:", balance)
            elif a == "2":
                amount = int(input("Deposit amount: "))
                user.deposit(amount)
                print("\t\tSuccessfully deposited.")
            elif a == "3":
                amount = int(input("withdraw amount : "))
                if user.withdrawa(amount):
                    print("\t\tWithdrawn Done.")
                else:
                    print("\t\tSorry you no enough money.")
            elif a == "4":
                friend_name = input("Enter the friend username: ")
                others = self.find_frnd(friend_name)
                if others:
                    amount = int(input("Enter transfer money: "))
                    if user.transfer_amount(others, amount):
                        print("\t\tTransferred Done.")
                    else:
                        print("\t\tSorry you no enough money.")
                else:
                    print("\t\tNot found your frnd.")
            elif a == "5":
                user.history_transaction()
            elif a == "6":
                if self.bank.loan_system:
                    amount = int(input("Enter loan money: "))
                    user.take_lone(amount)              
                else:
                    print("\t\tAdmin sir off this option now.")
    def find_user(self, username, password):
        for person in self.user_list:
            if person.username == username and person.password == password:
                return person
        return None   
    def find_frnd(self, username):
        for person in self.user_list:
            if person.username == username:
                return person
        return None
    
    def find_admin(self, username, password):
        for person in self.admin_list:
            if person.username == username and person.password == password:
                return person
        return None   
    
    def login(self):
        username = input("Enter Your Username: ")
        password = input("Enter a password: ")

        admin = self.find_admin(username, password)
        user = self.find_user(username, password)
        
        if user:
            self.user_menu(user)
        elif admin:  
            self.admin_menu(admin)
        else:
            print("\t\tNo user or admin found.")
        
b = system()
while True:          
    print("1. Create an account \n 2.Login to your account\n 3.EXIT")
    user_input = int(input("Enter Your option : "))
    if user_input ==3:
        break
    elif user_input ==1:
        b.create_account()
    elif user_input ==2:
        b.login()

   
'''
    Author : Kaushal Kishor
    github Link :- Github.com/curiousinvention
'''

        #Parent Class 
class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def show_detail(self):
        print("***************************")
        print("User Personal Detail")
        print(f"Name : {self.name}\nAge : {self.age}\nGender : {self.gender}")
        print("***************************")
        

        # Child Class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0
    
    def deposite(self,amount):
        self.amount = amount
        self.balance += self.amount
        print("\nDeposite Successful")
        print("Account Balance has been updated :- ₹",self.balance)

    def withdraw(self,amount):
        self.withdraw = amount
        if(self.balance < self.withdraw):
            print("Insufficiient Balance. | Balance Avilable :₹",self.balance)
        else:
            self.balance -= self.withdraw
            print("\nWithdrawl Successful")
            print("Account Balance has been Updates :- ₹",self.balance)

    def view_balance(self):
        self.show_detail()
        print("Current Account Balance :- ₹",self.balance)



# Get Input from user
newUser = Bank("Kaushal",21,"Male")
newUser.show_detail()

newUser.deposite(100)

newUser.deposite(100)
newUser.deposite(100)
newUser.deposite(700)

newUser.withdraw(300)

newUser.view_balance()



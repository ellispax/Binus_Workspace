import json
import atexit

filename = "bank.json"
user1 = ""
bal = ""

def login():
    global user1
    global bank
    print("***************************")
    print("-------MY BANK v1.01-------")
    print("***************************")
    
    username = input("--- UserName >> _ _")
    password = input("--- Password >> _ _")

    if (username == "ellis" and password == "pax"):
        admin_menu()
    elif username in bank.customers and (bank.getCustomer(username).getpass()) == password:
        user1 = bank.getCustomer(username)
        main()

    else:
        print("Invalid Credentials !!")
        login()
        
def create_menu():

    print("""\n
        *************************************
                    MY BANK v1.01
        *************************************
        Welcome """, user1.getname() ,"""
        *************************************
                    Choose Operation
        *************************************
                [1] Deposit
                [2] Withdraw
                [3] Check Balance
        -------------------------------------
                [Q] Quit
        *************************************
                -> """)
                
def admin_menu():
    def mnu():

        print("""\n
            *************************************
                        MY BANK v1.01
            *************************************
                WELCOME 
            *************************************
                        Choose Operation
            *************************************
                    [1] Add Customer
                    [2] Remove Customer
                    [3] Get Customer Info
                    [4] Get number of Customers
                    
            -----------------------
                    [Q] Quit
            *************************************
                    -> """)
    mnu()

    looper = 0
    while looper == 0:

        userInput = input()

        if (userInput == "1"):
            fname = input("Enter First Name >> ")
            lname = input("Enter Last Name >> ")
            paswd = input("Enter Password >> ")
            reenter = input("Re-enter your password >> ")
            usrname = input("Enetr prefferd username >>")

            if paswd != reenter:
                continue

            accnt = Account(100000)
            ini = Customer(fname, lname,paswd)
            ini.setaccount(accnt)
            bank.addCustomer(usrname, ini)
            print("Customer Account Successfully created !")
            mnu()

        elif(userInput == "2"):
            name = input("Enter Customer Username >> ")
            ans = input("Are you sure you want to delete record !! (Y/N) >> ")
            if ans.upper() == "Y":
                bank.remove(name)
                print("Record has been deleted !!")
                mnu()
            else:
                print("Operation Aborted !! ")
                mnu()
            

        elif(userInput == "3"):
            name = input("Enter Customer Username >> ")
            if name in bank.customers:

                here = bank.getCustomer(name)
                print("First Name >> ", here.getname())
                print("Last Name >> ", here.getlastname())
                print("Account Balance >> ", here.getaccount().getbal())
                print("Customer Username >> ", name)
                mnu()
            else:
                print("Customer not in the database !! ")
                mnu()
        
        elif(userInput == "4"):
            print("The total Number of Customers in the database is >> ", len(bank.customers))
            mnu()
            
                
        elif(userInput.upper() == "Q"):
            print("Are you sure you want to quit the program >> (Y/N)")
            ans = input()
            if(ans.upper() == "Y"):
                break
            else:
                print("Quiting Aborted")
        else:
            print("Invalid Input..")

def main():

    looper = 0
    while looper == 0:
    
        create_menu()
        
        userInput = input()

        if (userInput == "1"):
            amount = float(input("Enter Deposit Amount >> "))
            if amount > 0 :
                user1.getaccount().deposit(amount)
                print("RP", amount, "has been deposited into your acccount !")
            else:
                print("Invalid Deposit Amount !!")
    

        elif(userInput == "2"):
            userin = float(input("Enter Withdrawal amount >> "))
            if (userin > user1.getaccount().getbal()):
                print("Amount cannot be greater than the availale balance !")
            
            else:
                user1.getaccount().withdraw(userin)
                print("Your Account Balance is >> ", user1.getaccount().getbal())

        elif (userInput == "3"):
            print("Your Available Account Balance is >> ", user1.getaccount().getbal())
                    
        elif (userInput.upper() == "Q"):
            print("Are you sure you want to quit the program")
            print("Y/N >> ")
            exitans = input()
            if (exitans.upper() == "Y"):
                print("Thank you for banking with us.\nPlease feel free to get in touch with us for any help needed. ")
                looper += 1
            else:
                print("Quit aborted")

        else:
            print("Invalid Input !")
            print("Please enter a valid choice >> ")

def Loadjson():
    with open(filename, "r") as f:

        fil = json.load(f)
        bag = Bank(fil["bankname"])

        for key, value in fil["Customers"].items():
            dog = Customer(value["Firstname"], value["Lastname"], value["Pass"])
            dog.setaccount(Account(value["account"]["balance"]))
            bag.addCustomer(key, dog)

        return bag
            
def savejson():
    with open(filename, "w") as fp:
        fil = {}
        fil["bankname"] = bank.bankname
        fil["Customers"] = {}
        for username, data in bank.getall().items():
            fil["Customers"][username] = {
                "Firstname": data.getname(),
                "Lastname": data.getlastname(),
                "Pass": data.getpass(),
                "account": {
                    "balance": data.getaccount().getbal()
                }
            }
        json.dump(fil, fp, indent = 4)



class Account:
    def __init__(self, balance):
        self.balance = balance

    def getbal(self):
        return self.balance

    
    def deposit(self, amount):
        if (amount > 0):
            self.balance += amount

    def withdraw(self, amount):
        if (amount > 0 and amount < self.balance and self.balance - amount > 50000):
            self.balance -= amount


class Customer:
    account = None

    def __init__(self, Firstname, Lastname, Pass):
        self.Firstname = Firstname
        self.Lastname = Lastname
        self.Pass = Pass
    def getname(self):
       return self.Firstname

    def getlastname(self):
        return self.Lastname

    def getaccount(self):
        return self.account
    
    
    def getpass(self):
        return self.Pass
    def setaccount(self, x):
        self.account = x


class Bank:
    customers = {}
    def __init__(self, bankname):
        self.bankname = bankname
        
    def addCustomer(self, username, customer):
        self.customers[username] = customer

    def getnumCustomers(self):
        return len(self.customers)

    def getCustomer(self, username):
        return self.customers[username]

    def getall(self):
        return self.customers
    
    def remove(self, username):
        if username in self.customers:   
            del self.customers[username]



atexit.register(savejson)
bank = Loadjson()
login()


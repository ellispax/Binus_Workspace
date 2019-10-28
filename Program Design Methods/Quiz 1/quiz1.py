import json
import atexit
filename = 'C:/Users/Ellis_Pax/Documents/programming/Work_space/Quiz(23_10_19)/data.json'

looper = 0
    #23-October-2019 Quiz Solution
class Staff:
    __id = ""
    __name = ""
    __position = ""
    __salary = ""

    staff = {}
    def __init__(self, id, name, position, salary):
        self.__id = id
        self.__name = name
        self.__position = position
        self.__salary = salary
    
    def __eq__(self, strID):
        return self.__id == strID

    def getid(self):
        return self.__id

    def getname(self):
        return self.__name

    def getpos(self):
        return self.__position

    def getsal(self):
        return self.__salary
        
def loadjson():
        staff = []

        with open(filename, "r") as f:
            fill = json.load(f)
            for key , value in fill["Staff"].items():
                staff.append(Staff(key, value["Name"], value["Position"], value["Salary"]))
        return staff
positions = {
        "Staff": {
            "min": 3500000,
            "max": 7000000
        },
        "Officer": {
            "min": 7000001,
            "max": 10000000
        },
        "Manager": {
            "min": 10000001,
            "max": 1E+128
        }
    }     
staffs = loadjson()

def savejson():
        with open(filename,"w") as fp:
            fill = {
                "program_name": "Staff",
                "Staff": {}
            }
            for staff in staffs:
                fill["Staff"][staff.getid()] = {
                    "Name" : staff.getname(),
                    "Position": staff.getpos(),
                    "Salary": staff.getsal()
                }
            json.dump(fill, fp, indent = 4)
while looper == 0:   


    def printdata(staffs):
        data = [["ID", "Name", "Position", "Salary Amount"]]
        data += [[staff.getid(), staff.getname(), staff.getpos(), str(staff.getsal())] for staff in staffs]
        col_width = max(len(word) for row in data for word in row) + 2
        for row in data:
            print("|".join(word.ljust(col_width) for word in row))

    printdata(staffs)
    print("""\n
                [1] New Staff
                [2] Delete Staff
                [3] View Summary Data
                [4] Save & Exit """)

    userinput = input("Input Choice >> ")

    if (userinput == "1"):


        valid = False
        while (valid == False):
            validate = input("Input ID[SXXXX] >> ")
            
            valid = True
            if(validate[0] != "S"):
                print("Staff ID must have S as the first character")
                valid = False
                
            if (len(validate) != 5):
                print("Staff ID must be 5 characters long!")
                valid = False
                
            if validate in staffs:
                print("Staff ID already exists in database!")
                valid = False
            
            if(len(validate) > 5):
                print("Staff ID cannot be larger than 5 characters! ")
                valid = False
            
            
        
        name = input("Input Name(length < 20 characters) >> ")
        while (len(name) > 20):
            print("Name cannot be greater than 20 characters!")
            name = input("Input Name(length < 20 characters) >> ")
            

        position = input("Input Position > [Staff|Officer|Manager] >>")
        if (position.lower() == "staff"):
            salary = int(input("Input STAFF >> Salary (Rp3,500,000 - Rp7,000,000) >> "))
            while ((salary < 3500000) and (salary > 7000000)):
                print("Amount is out of range")
                salary = int(input("Input STAFF >> Salary (Rp3,500,000 - Rp7,000,000) >> "))

        elif (position.lower() == "officer"):
            salary = int(input("Input OFFICER >> Salary (Rp7,000,001 - Rp10,000,000) >> "))
            while ((salary < 7000001) and (salary > 10000000)):
                print("Amount is out of range")
                salary = int(input("Input OFFICER >> Salary (Rp7,000,001 - Rp10,000,000) >> "))
                
        elif (position.lower() == "manager"):
            salary = int(input("Input MANAGER >> Salary ( > Rp10,000,000) >> "))
            while (salary < 10000000):
                print("Amount is out of range")
                salary = int(input("Input MANAGER >> Salary ( > Rp10,000,000) >> "))

        staffs.append(Staff(validate, name, position, salary))
        print("Record has been saved! ")
        

    elif(userinput == "2"):
        print("Are you sure you want to delete a record?")
        ans = input("Yes (Y) or No (N) >> ")
        if ans.upper() == "Y":
            staffid = input("Enter Staff ID >>")
            if staffid not in staffs:
                print("Staff ID does not exist in database")
            else:
                staffs.pop(staffs.index(staffid))
        else:
            print("Delete Procedure Aborted !")

        
    elif(userinput == "3"):
        staffsal = []
        officersal = []
        managersal = []
        for staff in staffs:
            if staff.getpos() == "Staff":
                staffsal.append(int(staff.getsal()))
            elif staff.getpos() == "Officer":
                officersal.append(int(staff.getsal()))
            elif staff.getpos() == "Manager":
                managersal.append(int(staff.getsal()))
        printout = "1. Staff\n"
        printout += f"Minimum Salary: {positions['Staff']['min']}\n"
        printout += f"Maximum Salary: {positions['Staff']['max']}\n"
        try:
            printout += f"Average Salary: {sum(staffsal)/len(staffsal)}\n\n"
        except ZeroDivisionError:
            printout += "Average Salary: 0\n\n"

        printout += "2. Officer\n"
        printout += f"Minimum Salary: {positions['Officer']['min']}\n"
        printout += f"Maximum Salary: {positions['Officer']['max']}\n"
        try:
            printout += f"Average Salary: {sum(officersal)/len(staffsal)}\n\n"
        except ZeroDivisionError:
            printout += "Average Salary: 0\n\n"

        printout += "3. Manager\n"
        printout += f"Minimum Salary: {positions['Manager']['min']}\n"
        printout += f"Maximum Salary: {positions['Manager']['max']}\n"
        try:
            printout += f"Average Salary: {sum(managersal)/len(staffsal)}\n\n"
        except ZeroDivisionError:
            printout += "Average Salary: 0\n\n"
        print(printout)

    elif(userinput == "4"):
        print("Are you sure you want to Exit?")
        exitans = input("Yes (Y) or No (N) >> ")
        if exitans.upper() == "Y":
            print("Saving your Files .... >>> .....")
            print("Exiting ..... ... ... ...")
            savejson()
            looper += 1
        else:
            print("Exit Procedure Aborted!")
    else:
        print("Invalid Input !!")


 



    



atexit.register(savejson)




    

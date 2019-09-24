# Introduction to function
def addition(num_1, num_2):
    return int(num_1) + int(num_2)

def subtraction(num_1, num_2):
    return int(num_1) + int(num_2)

def multiplication(num_1, num_2):
    return int(num_1) * int(num_2)

def divide(num_1, num2):
    return int(num_1) / int(num_2)

def homework():
    firstNum = input("Enter your first number: ")
    secNum = input("Enter your second number: ")


    print("""\n
          *************************************
                Choose Preffered Operation
          *************************************
                [1] Addition
                [2] Subtraction
                [3] Multiplication
                [4] Division
          -----------------------
                [Q] Quit
          *************************************
                   -> """)
    
# Simple calculator
    userinput = input()

    if (userinput == "1"):
        total = addition(firstNum, secNum)
        print("The sum of your numbers is ", total)

    elif (userinput == "2"):
        diff = subtraction(firstNum, secNum)
        print("The difference betweenthe two numbers is ", diff)

    elif (userinput == "3"):
        product = multiplication(firstNum, secNum)
        print ("The product of the two Numers is ", product)
    elif (userinput == "4"):
        quotient = divide(firstNum, secNum)
        print("The result of teh division of the Numbers is ", quotient)
    
    elif (userinput.upper() == "Q"):
        print("\nQuiting ...\a\n   --Are you sure you want to quit ?")
        print("\n      :: Yes(Y) / No(N) **[Wrong input will be interpreted as a NO]**\n       -> ")
        exitAnswer = input()
        exitAnswer = exitAnswer.upper()
        if (exitAnswer == "YES" or exitAnswer == "Y"):
            return 1
        else:
            print("\n...Quit has been aborted\n")
    else:
        print("\n Bad or Unknown input ...\n")
        print("Please choose another option !\n  -- Press [Enter] to continue ")
    return 0


while True:
    value = homework()
    if(value == 1):
        break

exit("\n now Quitting program...\n")






    
    
# Task - create the remaining functions for substraction, multiplication and division
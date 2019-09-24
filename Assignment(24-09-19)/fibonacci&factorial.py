#%%
# Introduction to Recursive
# Recursion in computer science is a method of solving a problem where the solution
# depends on solutions to smaller instances of the same problem (as opposed to iteration).
#%%
# Program to display the Fibonacci sequence up to n-th term where n is provided by the user

nterms = int(input("How many terms? "))

# first two terms
n1 = 0
n2 = 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence upto",nterms,":")
   while count < nterms:
       print(n1,end=' , ')
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1



#%%
# Task: Create a function to calculate factorial value
def factorial(number):
    if(number > 1):
        return number * factorial(number-1)
    else:
        return number
    
print (factorial(4))
#%%
# Palindrome checking

str_tocheck = input("Enter your string: ")

def ispalindrome(input_str):
    return (input_str == input_str[::-1])

print (ispalindrome(str_tocheck))

# Task 1: Create a function to return a reversed string (e.g Input: asda; Output: adsa)
#%%
word = str(input("Enter the word >>"))

def reverse_word(x):
   for char in range(len(word) - 1, -1, -1):
           print(word[char], end="")
   print("\n")

sol = reverse_word(word)


#%%

# Task 2: Create a function to print the total of even numbers given an input of a list
# (e.g Input [0,3,4,5,6,7,9] Output 10)
#%%
numbers = []
qsn = int(input("How many number do you want to input >>"))
for i in range(qsn):
    number = int(input("Enter Number >>"))
    numbers.append(number)
    
print(numbers)
def calc_sum(numbers):
    total = 0
    for i in numbers:
        if(i % 2 == 0):
            total += i
    return total
    
ans = calc_sum(numbers)
print(ans)

#print(numbers)
#%%
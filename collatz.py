# A program that accepts a positive ineger from the user and applies the Collatz Conjecture to the given integer until the result reaches zero.
# Lehlogonolo Tshehla
# 19 March 2025

num = input("Enter a positive integer:\n")

if num.isdigit() and int(num) !=0:     # this checks if the user input is a number or not
    num = num.strip()
    num = int(num)
    n = num
    print(num,end=" ")
    while n != 1: # this ensures that the smallest the value of n can be is 1
        if n % 2 == 0: # this checks if the variable n is divisible by 2/ is an even number
            n = n/2 # this is taken from the given equation of what to do with even numbers
            print(round(n),end=" ")
            
        elif not(n % 2 == 0): # this will run when our variable becomes an odd number
            n = n * 3 + 1 # this is the formula we use when the variable is odd
            print(round(n),end=" ")    
elif num.isalpha():
    print("Invalid input. Please enter a valid integer.") # if the user gave bad input, such as words, we prompt them to give an actual number
else:
    print("Please enter a positive integer.") # this is carried out when the user gives us a number that is 0 or negative
    exit()

  
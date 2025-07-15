# A program that determines if a number given by the user is an Armstrong Number or not
# Lehlogonolo Tshehla
# 19 March 2025

num = input("Enter a number:\n")

size_num = 0 # the variable which will be used as an exponent

if num.isdigit():     # this checks if the user input is a number or not
    size_num = len(num)    # we assign the length of the string of the user's number to the variable
    numz = int(num)
    n = 0
    nn = 0
    
    for i in num: # we will iterate through the string that the user gave as numbers
        i = int(i) # this will convert those string numbers into integer numbers
        n = i ** size_num # this raises the single integer value by the length of the string number 
        nn = nn + n # this is how we find out if the user gave a number that is an Armstrong number
    
    if nn == numz:
        print(num,"is an Armstrong number.")
    else:
        print(num,"is not an Armstrong number.")        
else:
    print("Invalid input. Please enter a valid integer.")# if the user gave bad input, we prompt them to give the correct number
    exit()


# A program that accepts a starting number followed by the number of rows amd columns and prints it in the form of a grid
# Lehlogonolo Tshehla
# 20 March 2025

number = input("Enter the starting number (n):\n") # this asks for the number which will be used as the staring point of the grid

if number.isalpha() or int(number) < 0:
    print("Invalid input. Please enter integers.")
    number = input("Enter the starting number (n):\n")
    while number.isalpha() or int(number) < 0:
        print("Invalid input. Please enter integers.")
        number = input("Enter the starting number (n):\n")
    
rows = input("Enter the number of rows (r):\n")

if (rows.isalpha() or int(rows) < 0):
    print("Rows and columns must be positive integers.")
    number = input("Enter the starting number (n):\n")
    rows = input("Enter the number of rows (r):\n")
    columns = input("Enter the number of columns (c):\n")      
    while rows.isalpha() or int(rows) < 0:
        print("Invalid input. Please enter integers.")
        number = input("Enter the starting number (n):\n")
        rows = input("Enter the number of rows (r):\n")

columns = input("Enter the number of columns (c):\n")

if (columns.isalpha() or int(columns) < 0):
    print("Rows and columns must be positive integers.")
    number = input("Enter the starting number (n):\n")
    rows = input("Enter the number of rows (r):\n")
    columns = input("Enter the number of columns (c):\n")      
    while columns.isalpha() or int(columns) < 0:
        print("Invalid input. Please enter integers.")
        number = input("Enter the starting number (n):\n")
        rows = input("Enter the number of rows (r):\n")
        columns = input("Enter the number of columns (c):\n")


n = int(number) - 1 # this allows the starting number to be included in the grid without altering the rows or columns

r = int(rows)

c = int(columns)

for x in range(r): # this loop that will create the number of rows while iterating through the starting number
    
    for z in range (c): # this lop will create the number of columns that contain the numbers we added to the starting number
       
        n += 1
        
      
        print(str(n).rjust(3),end=" ")
   
    print(" ") # this allows the loop to loop back onto itself
    
# A program that takes a list of arbitrary numbers but it removes any deplicates and returns the same list but without the duplicates
# Lehlogonolo Tshehla
# 22 March 2025

arrays = [] # this is the array that will collect the array of the rows of the grid
rows = [] # this is the array of the rows
row = 0
columns = [] # this is the array that will collect rows array
print("Enter an array:")
for r in range(9):
    row = input( )
    rows.append(row)
    if len(rows) == 9:
        break
for r in rows:
    for c in r:
        c = int(c)
        columns.append(c)
    arrays.append(columns)
    columns = []

        
x = 1 # lines 35 and 36 are are arbitriary values assigned to the varibales that will be used as coordinates
y = 1

while True: # this while loop is there to continuously ask for the coordinates provided by the user until they give negative values
    coord = input("Enter coordinates:\n").strip()
    coord = coord.split(" ")
    x = int(coord[0])
    y = int(coord[1])
    if x >= 0 and y >= 0: # if the coordinates are greater or eqaul to 0, then the print statement is carried out
        print("Value =",arrays[x][y])
    else: # this will break the loop if the coordinates are negative
        print("DONE")
        break
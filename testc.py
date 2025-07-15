# A program that asks the user to enter a series of comma-separated integer numbers. The program will count the number of adjacent pairs of values where the first number is a factor of the second number in the sequence
# Lehlogonolo Tshehla
# 08 April 2025

numbs = input("Enter a comma-separated list of numbers:\n")
numbs = numbs.split(",")
numb = []
counts = []

for x in numbs:
    x = int(x)
    numb.append(x)
count = 0
x = 0
y = 1
a = numbs[x]
b = numbs[y]

for x in numbs:
    if a % b == 0:
        count+=1
    else:
        a = numbs[x+1]
        b = numbs[y+1]

for b in numb:
    for a in numb:
        if b % a == 0:
            count += 1    
        else:
            continue
        counts.append(count)
        count = 0

print("Number of adjacent pairs where the 1st number is a factor of the 2nd number:",count)
# A program that  asks the user to enter a series of comma-separated integer numbers. The program should count all adjacent pairs where the second number is strictly greater than the first
# Lehlogonolo Tshehla
# 15 April 2025

num = input("Enter a comma-separated list of numbers:\n")

num = num.split(",")

count = 0 

for pair in range(len(num)-1):
    if int(num[pair]) < int(num[pair+1]):
        count += 1
        
print(f"Number of pairs of numbers where 2nd is strictly greater than 1st: {count}.")
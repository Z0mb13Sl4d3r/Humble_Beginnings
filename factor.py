# A program that asks tyhe user to enter a number and asks for that many numbers to be put into a list. Then asks for a factor to which we fill find what is a factor in that list
# Lehlogonolo Tshehla
# 25 March 2025

numbs = int(input("How many numbers?\n"))

array = []
factors = []

for n in range(numbs):
    numb = int(input("Enter a number:\n"))
    array.append(numb)
print(f"The numbers are: {array}.")

fact = int(input("Enter the factor:\n"))

for l in array:
    l = int(l)
    if fact == 1:
        factors.append(l)
    
    elif l % fact == 0:
        factors.append(l)
    

print(f"The numbers with that factor are: {factors}.")
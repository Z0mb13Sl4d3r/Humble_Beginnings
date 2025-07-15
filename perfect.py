# A program that determines all the proper divisors of a number and displaces whether it is a perfect number or not
# Lehlogonolo Tshehla
# 09 March 2025

number = int(input("Enter a number:\n"))
count = 1
sum_of_factors = 0
print(f"The proper divisors of {number} are:")
while count< number: # lines 8 to 12 were inspired and referenced from Chat GPT and then altered by myself
    if number % count == 0:
        print(count,sep=" ",end=" ")
        sum_of_factors += count
    count +=1
print(" \n")
if sum_of_factors == number:
    print(number,"is a perfect number.")
else:
    print(number,"is not a perfect number.")
        

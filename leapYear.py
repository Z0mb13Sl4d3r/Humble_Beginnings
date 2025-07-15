# A program that determines whether a year entered by the user is a leap year or not 
# Lehlogonolo Tshehla
# 25 February 2025

year = int(input("Enter a year:\n"))

if year%400==0:
    print(year,"is a leap year.")

elif year%4==0 and not year%100==0:
    print(year,"is a leap year.")

else:
    print(year,"is not a leap year.")

# A program that checks if the time received from the user as a set of 3 integers is valid
# Lehlogonolo Tshehla
# 25 February 2025

hours = int(input("Enter the hours:\n") )

minutes = int(input("Enter the minutes:\n"))

seconds = int(input("Enter the seconds:\n"))

if hours >= 24 or hours < 0:
    print("Your time is invalid.")

elif minutes >= 60 or minutes < 0:
    print("Your time is invalid.")

elif seconds >= 60 or seconds < 0 :
    print("Your time is invalid.")

else:
    print("Your time is valid.")

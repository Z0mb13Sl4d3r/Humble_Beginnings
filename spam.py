# A program that generates a personalised spam message using the user's name, surname, the amount of money they want amd the country they are from
# Lehlogonolo Tshehla
# 25 February 2025

first_name = input("Enter first name:\n") 

last_name = input("Enter last name:\n")

money = int(input("Enter sum of money in USD:\n"))

country = input("Enter country name:\n")

money30 = (30*money)/100

print("")

print(f"Dearest {first_name}")
print(f"It is with a heavy heart that I inform you of the death of my father,\nGeneral Fayk {last_name}, your long lost relative from Mapsfostol.\nMy father left the sum of {money}USD for us, your distant cousins.\nUnfortunately, we cannot access the money as it is in a bank in {country}.\nI desperately need your assistance to access this money.\nI will even pay you generously, 30% of the amount - {money30}USD,\nfor your help.  Please get in touch with me at this email address asap.")

print("Yours sincerely")

print(f"Frank {last_name}")
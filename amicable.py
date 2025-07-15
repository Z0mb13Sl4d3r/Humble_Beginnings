# A program that determines if two numbers given by the user are amicable to each other
# Lehlogonolo Tshehla
# 11 March 2025

number1 = int(input("Enter first number:\n"))
number2 = int(input("Enter second number:\n"))
count1 = 1
count2 = 1
sum_of_factor1 = 0
sum_of_factor2 = 0

while count1< number1: # lines 11 to 14 were inspired and referenced from Chat GPT and then altered by myself
    if number1 % count1 == 0:
        sum_of_factor1 += count1
    count1 +=1
while count2< number2: # lines 11 to 14 were inspired and referenced from Chat GPT and then altered by myself
    if number2 % count2 == 0:
        sum_of_factor2 += count2
    count2 +=1

if sum_of_factor1 == number2 and sum_of_factor2 == number1:
    print(number1,"and",number2,"are amicable numbers.")
else:
    print(number1,"and",number2,"are not amicable numbers.")

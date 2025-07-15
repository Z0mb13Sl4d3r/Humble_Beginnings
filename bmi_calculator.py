# A program that calculates a person's BMI using their inputs on their weight and height and categorizes their BMI based on the data given
# Lehlogonolo Tshehla
# 27 February 2025

weight = eval(input("Enter your weight in kg:\n"))

height = eval(input("Enter your height in meters:\n"))

bmi = weight/(height**2)

print("Your BMI is",round(bmi,2))

if bmi < 18.5:
    print("Category: Underweight")

elif 18.5 <= bmi <24:
    print("Category: Normal weight")

elif 25 <= bmi < 29:
    print("Category: Overweight")

else:
    print("Category: Obese")


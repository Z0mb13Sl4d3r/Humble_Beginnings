# A program that calculates how long a light signal emitted takes to bounce back off of water levels
# Lehlogonolo Tshehla
# 03 March 2025
from math import pi
time = eval(input("Enter the travel time (milliseconds):\n"))
temperature = eval(input("Enter the air temperature (Centigrade):\n"))
temperature = round(temperature,1)

tank = 4.27
sensor = 0.5
level_cal = (331.3 + 0.606*temperature)*time/2000 - sensor
level_cal = round(level_cal,2)
level = tank - level_cal
print("The water level is %.2f." % level)

red = (tank * 10/1000)
red = round(red,3)
orange = (tank * 50/100)
orange = round(orange,3)
yellow = (tank * 75/100)
yellow = round(yellow,3)

if level <= red:
    print("Light: Red")
elif red < level <= orange:
    print("Light: Orange.")
elif orange < level <= yellow:
    print("Light: Yellow.")
elif level > yellow:
    print("Light: Green.")
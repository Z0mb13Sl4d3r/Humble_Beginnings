# A program that takes in the radius given by the user and gives out the volume
# Lehlogonolo Tshehla
# 15 April 2025

from math import pi, pow

def volume(radius):
            vol = ( 4 * pi*pow(radius,3)/3)
            return vol
def main():
            radius = eval(input("Enter the radius of the sphere:\n"))
            if radius > 0:
                        print("The volume is %.2f." % volume(radius))
                        
            else:
                        print("The radius must not be a negative value.")
      

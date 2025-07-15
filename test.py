# A program that calculates the lift force using a inout data from the users on a, rho, v, R_e, A and F_L
# Lehlogonolo Tshehla
# 04 March 2024

rho = eval(input("Enter the value of the air density, rho:\n"))
v = eval(input("Enter the value of the velocity or true airspeed, v:\n"))
R_e = eval(input("Enter the value of the lift coefficient, R_e:\n"))
A = eval(input("Enter the value of the Reference Area, A:\n"))

if R_e<0:
    print("Wrong number")

F_L = 1/2*(rho*v**2)*A*24/R_e
F_L = round(F_L)
print(f"The lift force, F_L, is {F_L}.")
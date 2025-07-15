# A program that accepts an input value for precision, and computes and outputs an estimate for the golden ratio
# Lehlogonolo Tshehla
# 11 March 2025

precision = eval(input("Enter a value for the required precision:\n"))

e_0 = 1
e_n = 2

while True  :
    e_0 = e_n
    e_n = 1+1/e_0
    e_d = abs(e_n - e_0)
    if e_d < precision:
        break

print("The estimate is %.3f." %e_n)
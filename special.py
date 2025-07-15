# A program that asks the user to enter a string of characters and that extracts and prints all substrings that are NOT composed of letters
# Lehlogonolo Tshehla
# 08 April 2025

sentence  = input("Enter the string of characters:\n")
numbs = ["0","1","2","3","4","5","6","7","8","9"]
xx = ""
xv = ""

for s in sentence:
    for n in numbs:
        if n == s:
            s = n
            xx = sentence.find(s)
            xv = sentence.find(s)
            

# v26sal%(@@!a3gah:
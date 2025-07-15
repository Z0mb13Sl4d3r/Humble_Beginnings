# A program that takes a list of arbitrary numbers but it removes any deplicates and returns the same list but without the duplicates
# Lehlogonolo Tshehla
# 22 March 2025

numbers  = input("Enter an array of numbers (separated by spaces):\n")
numbers = numbers.split(" ")

num_array = [] # this is the array that will contain our unduplicated list of numbers from the user
numb = {} # this is what is used to record the numbers that are in the user input without the duplications

for n in numbers: # this for loop iterates through the list of user input and uses them as keys to be put into a dictionary
   if n in numb:
      numb[n] += 1 # this adds 1 to any number that is already a key in the dictionary created
   else:
      numb[n] = 1 # this assigns the value 1 to any new keys in the dictionary

for keys in numb.keys(): # this is how we get a array of all the numbers from the user without any duplications
   keys = int(keys)
   num_array.append(keys)
    
print("Unique element array:",num_array)
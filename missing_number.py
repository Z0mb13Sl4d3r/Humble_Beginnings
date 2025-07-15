# A program that takes a list of arbitrary numbers and outputs the missing number
# Lehlogonolo Tshehla
# 21 March 2025

array = input("Enter an array of numbers (separated by spaces):\n") # this is what we use to accept user input

array = array.split(" ") # this allows us to create an array of the numbers given by seperating the elements by the spaces between the numbers

arr = [] # this is the new list that we will use to find the smallest and biggest number in the original list/array

sum1 = 0 # from line 11 to 13 are variables which will be changed to the smallest, biggest and the difference between the two respectively
sum2 = 0
diff = 0

for x in array: # this is the loop that will add up all the numbers given by the user
    sum1 += int(x)
for a in array: # this is the loop that will append all the converted elements of the original into a list of integers 
    a = int(a)
    arr.append(a)

arr.sort() # this sorts the elements of the new from ascending order
mini = arr[0]
maxi = arr[-1]
for i in range(mini,maxi+1): # this will add up the range of the smallest number in the array to the biggest in the array
    sum2 += i

diff = sum2 - sum1 # this subtracts the two sums found to find the number that is missing in the array
if diff != 0:
    print("Missing number:",diff)
else:
    print("There is no missing number.")

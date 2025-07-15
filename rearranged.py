# A program that takes a list of arbitrary numbers and outputs a sorted array of numbers such that the first number is the biggest, the second is the smallest and the third number is the 2nd biggets then followed by the rest of the numbers
# Lehlogonolo Tshehla
# 22 March 2025

numbers = input("Enter sorted numbers separated by spaces:\n") # this asks for the numbers from the user in order to start the sorting 

numbers = numbers.split(" ") # this converts the numbers given and turns it into a list that we will use to find the numbers we want

numb_array = [] # this empty array is the one which we will store the numbers after removing the whitespaces 

for n in numbers:
    n = int(n)
    numb_array.append(n)

def rearrange(arr):
    if not arr:  # If the user gives an empty list, we just return that list
        return
    
    n = len(arr)
    low, high = 0, n - 1
    temp = arr[:]  # This temporarily stores the list given by the user
    toggle = True  # This changes between the biggest and smallest elements in the list
    
    for i in range(n):
        if toggle:
            arr[i] = temp[high]  # This allows us to pick the biggest element in the list
            high -= 1
        else:
            arr[i] = temp[low]  # This allows us to pick the smallest element in the list
            low += 1
        toggle = not toggle  # This changes out Boolean from a True to a False

if __name__ == "__main__":  # The sorted array
    rearrange(numb_array)
    print("Rearranged array:",numb_array)

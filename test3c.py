# A recursive program to swap two consecutive elements in an array.

# Your Name here
# Lehlogonolo Tshehla
# 09 May 2023

import sys
sys.setrecursionlimit (30000)

def swap_elements(A, start_index=0):
    if len(A) == 0:
        return print(-1)
    else:
        arr = []
        if start_index < len(A)-2:
            arr.append(A[start_index+1])
            arr.append(A[start_index])
            arr = arr + A[start_index+2:]
            return arr

def main():
    # accept user input
    A = input("Enter the elements of the array separated by commas:\n")
    
    # swap the consecutive elements
    result = swap_elements(list(map(int, A.strip().split(","))))
    # display the result
    print("The array with consecutive elements swapped is:")
    print(result)


if __name__ == '__main__':
    main()
##1, 5, 9, 7, 3, 2, 4, 8, 6
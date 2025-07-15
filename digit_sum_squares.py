# A program that recursively finds and prints all numbers between two given integers M and N (inclusive) such that the sum of the squares of their digits is a prime number
# Lehlogonlo Tshehla
# 08 May 2025

def downcreasing(w):
    if w == 0:
        return w
    else:
        return downcreasing(w+1)

def is_prime(num, divisor=2): # this returns the numbers that are prime numbers
    # Recursive prime check
    if n < 2:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return is_prime(n, divisor+1)


def main():
    start = int(input("Enter the starting point M:\n"))
    end = int(input("Enter the ending point N:\n"))
    length = str(start)
    word = -len(length)+1   

if __name__ == "__main__":
    main()
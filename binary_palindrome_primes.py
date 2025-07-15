# A program that  recursively finds and prints all prime numbers between two integers whose binary representations are also palindromes
# Lehlogonolo Tshehla
# 28 April 2025

import sys 
sys.setrecursionlimit (30000)

def is_prime(n, divisor=2): # this returns the numbers that are prime numbers
    # Recursive prime check
    if n < 2:
        return 
    if divisor * divisor > n:
        return n
    if n % divisor == 0:
        return 
    return is_prime(n, divisor+1)
            

def to_binary(n): # this returns the binary value of the prime number
    # Recursive integer to binary string
    if n < 2:
        return str(n)
    else:
        return to_binary(n // 2) + str(n % 2)
    

def is_palindrome(s,i=0,f=-1): # returns a True if the binary of a prime is a palindrome
    # Recursive string palindrome check
    if not s:
        return True
    if len(s) == 1:
        return True
    if s[i] != s[f]:
        return False
    else:
        return is_palindrome(s[i+1:f])

def search_palindromic_primes(n, m):
    # Recursive range traversal
        n = int(n)
        m = int(m)
        if n > m:
            return
        if is_prime(n) == None:
            return search_palindromic_primes(n+1,m)
        else:
            if is_palindrome(to_binary(is_prime(n))) == False :
                return search_palindromic_primes(n+1,m)
            else:
                print(f"{is_prime(n)} (binary: {to_binary(is_prime(n))})")
                return search_palindromic_primes(n+1,m)
                
        

def main():
    # your code here
    m = int(input("Enter the starting point M:\n"))
    n = int(input("Enter the ending point N:\n"))
    print(f"Binary palindrome primes between {m} and {n} are:")
    search_palindromic_primes(m, n)
    
# Main block to take input and start the recursive search
if __name__ == "__main__":
    main()


def is_prime(n, divisor=2): # this returns the numbers that are prime numbers
    # Recursive prime check
    if n < 2:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return is_prime(n, divisor+1)

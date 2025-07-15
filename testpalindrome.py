# A program that achieves path coverage and tests the module of "is_palindrome" and has a set of test cases to achieve statement coverage
# Lehlogonolo Tshehla
# 22 April 2025

"""
>>> import palindrome
>>> palindrome.is_palindrome("racecar")
True
>>> palindrome.is_palindrome("R")
True
>>> palindrome.is_palindrome("181")
True
>>> palindrome.is_palindrome("Hello Im superman")
False
>>> palindrome.is_palindrome(False)
True

"""
import doctest 
doctest.testmod(verbose=True)

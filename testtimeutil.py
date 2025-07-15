# A program that achieves statement coverage and tests the module of "timeutil" and has a set of test cases to achieve statement coverage
# Lehlogonolo Tshehla
# 23 April 2025

"""
>>> import timeutil
>>> timeutil.validate("0515 p.m.")
False
>>> timeutil.validate("111:30 p.m.")
False
>>> timeutil.validate("03:55 a.m.")
False
>>> timeutil.validate("6:30 pm")
False
>>> timeutil.validate("9:2 a.m.")
False
>>> timeutil.validate("8:00 p.m.")
True

"""

import doctest 
doctest.testmod(verbose=True)
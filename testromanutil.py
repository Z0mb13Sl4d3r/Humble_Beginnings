# A program that achieves path coverage and tests the module of "romanutil" and has a set of test cases to achieve path coverage
# Lehlogonolo Tshehla
# 21 April 2025

"""
>>> import romanutil
>>> romanutil.from_roman("X")
10
>>> romanutil.from_roman("IV")
4
>>> romanutil.from_roman("DV")
505
>>> romanutil.from_roman("VVV")
15
>>> romanutil.from_roman("XCM")
890
>>> romanutil.from_roman("IMVL")
1044

"""

import doctest 
doctest.testmod(verbose=True)
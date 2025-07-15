# A program that achieves path coverage and tests the module of "triangle" and has a set of test cases to achieve path coverage
# Lehlogonolo Tshehla
# 22 April 2025

"""
>>> import triangle

>>> triangle.classify_by_angle(3,4,5)
'right'
>>> triangle.classify_by_angle(-3,3,5)
'obtuse'
>>> triangle.classify_by_angle(-3,-6,5)
'acute'
>>> triangle.classify_by_angle(-3,6,-5)
'obtuse'
>>> triangle.classify_by_angle(3,5,4)
'right'
>>> triangle.classify_by_angle(-3,6,-50)
'acute'
>>> triangle.classify_by_angle(8,5,6)
'obtuse'
>>> triangle.classify_by_angle(5,3,4)
'right'
>>> triangle.classify_by_angle(8,-6,-7)
'acute'

"""

import doctest 
doctest.testmod(verbose=True)
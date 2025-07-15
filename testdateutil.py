# A program that achieves path coverage and tests the module of "dateutil" and has a set of test cases to achieve path coverage
# Lehlogonolo Tshehla
# 20 April 20255


"""
>>> import dateutil
>>> dateutil.format_date(5,14,2006)
'Invalid date'
>>> dateutil.format_date(35,5,2006)
'Invalid date'
>>> dateutil.format_date(35,4,2006)
'Invalid date'
>>> dateutil.format_date(5,4,2006)
'5 April 2006'
>>> dateutil.format_date(5,3,2006)
'5 March 2006'
>>> dateutil.format_date(30,2,2006)
'Invalid date'
>>> dateutil.format_date(30,2,2008)
'Invalid date'
>>> dateutil.format_date(5,2,2006)
'5 February 2006'
>>> dateutil.format_date(5,2,2008)
'5 February 2008'

"""

import doctest 
doctest.testmod(verbose=True)
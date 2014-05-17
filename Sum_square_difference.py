# -*- coding: utf-8 -*-
#
# The sum of the squares of the first ten natural numbers is,
# 
# 1² + 2² + ... + 10² = 385
# The square of the sum of the first ten natural numbers is,
# 
# (1 + 2 + ... + 10)² = 55² = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.
# 
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sum_squares = sum([n ** 2 for n in xrange(1,101)])

square_sums = sum([n for n in xrange(1,101)]) ** 2

print sum_squares - square_sums

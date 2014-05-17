# -*- coding: utf-8 -*-
# A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
# 
# a² + b² = c²
# For example, 3² + 4² = 9 + 16 = 25 = 5².
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def isTriplet(a,b,c):
    if (a**2 + b**2) == c**2:
        return True
    return False

for i in xrange(1,1000):
    for j in xrange(1,1000):
        for k in xrange(1,1000):
            if isTriplet(i,j,k):
                if i+j+k == 1000:
                    print i*j*k
                    exit(0)

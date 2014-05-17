# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# 
# What is the 10 001st prime number?

from numpy import sqrt
import timeit

def primeGen1(lim):
    """Generate Primes up to limit"""
    pp = 2
    ps = [pp]
    while pp < lim:
        pp += 1
        for a in ps:
            if pp % a == 0:
                break
        else:
            ps.append(pp)
    return  ps

def primeGen2(lim):
    pp = 2
    ps = [pp]
    pp += 1
    ps.append(pp)
    while pp < lim - 1:
        pp += 2
        test = True
        for a in ps:
            if pp % a == 0:
                test = False
                break
        if test: ps.append(pp)
    return ps

def primeGen3(lim):
    """Generate Primes up to limit"""
    pp = 2
    ps = [pp]
    pp += 1
    ps.append(pp)
    
    while pp < lim - 1:
        pp += 2
        test = True
        sqrtpp = sqrt(pp)
        for a in ps:
            if a > sqrtpp: break
            if pp % a == 0:
                test = False
                break
        if test: ps.append(pp)
    return ps

num=1000000

print timeit.timeit("primeGen1(num)", setup="from __main__ import primeGen1, num", number = 100)
print timeit.timeit("primeGen2(num)", setup="from __main__ import primeGen2, num", number = 100)
print timeit.timeit("primeGen3(num)", setup="from __main__ import primeGen3, num", number = 100)
#print timeit.timeit(getNum2, number=100)/100

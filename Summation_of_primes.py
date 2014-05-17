# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

from numpy import sqrt

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
        if test:
            ps.append(pp)
            yield pp
    #return ps

total = 5
for i in primeGen3(2000000):
#    print i
    total += i
print total

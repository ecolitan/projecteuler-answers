# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def testDivisibility(n):
    for i in xrange(1,21):
        if n % i != 0:
            return False
    return True

m = 1
while testDivisibility(m) is False:
    m += 1

print m

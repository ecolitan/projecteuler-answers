# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?

num = 600851475143

primes = []
testnum = 2

while num != 1:
    rest = num % testnum
    if (rest == 0):
        primes.append(testnum)
        num = num / testnum
    else:
        while rest != 0:
            testnum += 1
            rest = num % testnum
        primes.append(testnum)
        num = num / testnum

print primes

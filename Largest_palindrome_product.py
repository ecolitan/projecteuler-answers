# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.

# 906609

import timeit

def isPalindromic(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False

def getNum1():
    # method 1
    largest = 0
    
    for i in xrange(999,100,-1):
        for j in xrange(999,100,-1):
            k = i*j
            if isPalindromic(k):
                # method 1
                if k > largest:
                    largest = k            
    return largest

def getNum2():
    # method 1
    l = []
    
    for i in xrange(999,100,-1):
        for j in xrange(999,100,-1):
            k = i*j
            if isPalindromic(k):
                # method 1
                l.append(k)
    return sorted(l)[-1]


print timeit.timeit(getNum1, number=100)/100
print timeit.timeit(getNum2, number=100)/100

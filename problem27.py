
import math
import euler
import time
def quad(n,a,b):
    return (n**2) + (a*n) + b
primes = euler.sieve(100000)
count = 0
max = 0
ans = 0
start = time.time()
for x in xrange(-999,0,2):
    for i in xrange(1,1000,2):
        while quad(count,x,i) in primes:
            count+=1
        if count > max:
            ans = x*i
            max = count
            print ans
        count = 0
print max, time.time()-start

__author__ = "dpalaci0s"
import time
start = time.time()
sum = 0
outerSum = 0
for x in xrange(2,5*9**5):
    max = len(str(x))
    for i in xrange(0,max):
       sum+=(int(str(x)[i])**5)
    if sum == x:
        outerSum+=x
    sum = 0
print outerSum, time.time()-start

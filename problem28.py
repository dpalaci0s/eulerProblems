sum = 1
count = 0
num = 3
step = 2
while num <=1001**2:
    sum+=num
    count+=1
    if count == 4:
        step+=2
        count = 0
    num+=step
print sum

#https://projecteuler.net/problem=9
import math
def isPrime(n):
    res = True
    if(n<=1):
        res = False
    if(n%2==0 and n!=2):
        res = False
    for i in range(3,round(math.sqrt(n))+1,2):
        if(n%i==0):
            res = False
    return(res)
sum=0
for i in range(2000000):
    if(isPrime(i)):
        sum+=i
print(sum)
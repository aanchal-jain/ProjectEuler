def countDivisors(n):
    res=[1,n]
    for i in range(2,n//2+1):
        if(n%i==0):
            res.append(i)
    return(len(res))
countDivisors(28)
x = 55
y = 11
while(countDivisors(x)<=500):
    x+=y
    y+=1
print(x)

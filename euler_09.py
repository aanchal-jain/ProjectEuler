#https://projecteuler.net/problem=9
for a in range(500):
    for b in range(500):
        for c in range(500):
            if(a+b+c==1000 and a**2+b**2==c**2):
                print(a*b*c)
                
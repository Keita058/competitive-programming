from math import gcd

N=int(input())
A=list(map(int,input().split()))

GCD=gcd(*A)
if GCD==1:
    print(2)
else:
    print(1)
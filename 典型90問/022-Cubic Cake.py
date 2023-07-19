from math import gcd

a,b,c=map(int,input().split())

GCD=gcd(a,gcd(b,c))

a//=GCD
b//=GCD
c//=GCD

print(a+b+c-3)
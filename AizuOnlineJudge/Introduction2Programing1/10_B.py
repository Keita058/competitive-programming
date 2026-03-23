import math
a,b,c=map(int,input().split())
S=a*b*math.sin(math.radians(c))/2
x=(a**2+b**2-2*a*b*math.cos(math.radians(c)))**0.5
L=a+x+b
h=2*S/a
print(round(S,5))
print(round(L,5))
print(round(h,5))
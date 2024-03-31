D=int(input())

x=0
ans=float('inf')
while x**2<=D:
    y=int((D-x**2)**0.5)
    ans=min(ans,abs(x**2+y**2-D))
    ans=min(ans,abs(x**2+(y+1)**2-D))
    x+=1
print(ans)

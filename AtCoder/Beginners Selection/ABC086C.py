N=int(input())
t0,x0,y0=0,0,0
flag=True
for i in range(N):
    t,x,y=map(int,input().split())
    dist=abs(x0-x)+abs(y0-y)
    if dist==0:
        dist=2
    time=t-t0
    if time%dist!=0:
        flag=False
    t0,x0,y0=t,x,y
print('Yes' if flag else 'No')
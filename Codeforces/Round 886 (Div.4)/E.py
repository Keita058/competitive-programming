def is_ok(x,p,q,r):
    return p*x**2+q*x+r>=0

def bisect(ok,ng,p,q,r):
    while abs(ok-ng)>1:
        mid=(ok+ng)//2
        if is_ok(mid,p,q,r):
            ok=mid
        else:
            ng=mid
    return ok


t=int(input())
for _ in range(t):
    n,c=map(int,input().split())
    s=list(map(int,input().split()))
    a=b=0
    for i in range(n):
        a+=s[i]**2
        b+=s[i]
    ans=bisect(10**18,0,4*n,4*b,a-c)
    print(ans)

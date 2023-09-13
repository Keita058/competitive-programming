N=int(input())

if N%2==1:
    print(0)
else:
    ans=0
    x=5
    while x<=N:
        cnt=N//x
        x*=5
        ans+=cnt//2
    print(ans)
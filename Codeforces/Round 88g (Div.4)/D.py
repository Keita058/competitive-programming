t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    leng=0
    cnt=1
    for i in range(n-1):
        if abs(a[i]-a[i+1])<=k:
            cnt+=1
        else:
            leng=max(cnt,leng)
            cnt=1
    leng=max(cnt,leng)
    print(n-leng)
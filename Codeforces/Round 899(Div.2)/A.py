t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=[ i+1 for i in range(n)]
    min_b=min(b)
    for i in range(n):
        if i>0:
            if b[i]<=b[i-1]:
                b[i]=min_b+1
        if a[i]==b[i]:
            b[i]+=1
        min_b=b[i]
    print(b[-1])
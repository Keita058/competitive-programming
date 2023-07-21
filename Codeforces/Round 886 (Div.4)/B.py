t=int(input())
for _ in range(t):
    n=int(input())
    ans=1
    quality=0
    for i in range(n):
        a,b=map(int,input().split())
        if a<=10 and quality<b:
            ans=i+1
            quality=b
    
    print(ans)

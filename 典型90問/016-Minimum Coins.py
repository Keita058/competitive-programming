N=int(input())
a,b,c=map(int,input().split())

ans=float('inf')
for i in range(10**4):
    for j in range(10**4):
        if i+j>=10**4:
            break
        if (N-(a*i+b*j))%c==0 and N>=a*i+b*j:
            k=(N-(a*i+b*j))//c
            ans=min(ans,i+j+k)

print(ans)
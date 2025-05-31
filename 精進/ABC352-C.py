N=int(input())
AB=[]
for i in range(N):
    a,b=map(int,input().split())
    AB.append((b-a,a,b))

AB.sort()
ans=0
for i in range(N):
    c,a,b=AB[i]
    ans+=a
    if i==N-1:
        ans+=c

print(ans)
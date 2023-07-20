N,Q=map(int,input().split())
A=list(map(int,input().split()))
B=[0 for _ in range(N-1)]
ans=0
for i in range(N-1):
    B[i]=A[i+1]-A[i]
    ans+=abs(B[i])

for _ in range(Q):
    l,r,v=map(int,input().split())
    if l==1 and r==N:
        print(ans)
        continue
    if l==1 and r<N:
        mae=abs(B[r-1])
        B[r-1]-=v
        ato=abs(B[r-1])
    if l>1 and r==N:
        mae=abs(B[l-2])
        B[l-2]+=v
        ato=abs(B[l-2])
    if l>1 and r<N:
        mae=abs(B[l-2])+abs(B[r-1])
        B[r-1]-=v
        B[l-2]+=v
        ato=abs(B[l-2])+abs(B[r-1])
    ans+=ato-mae
    print(ans)
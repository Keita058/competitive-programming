N=int(input())
S=input()

A=[[0,0] for _ in range(N+1)]
for i in range(N):
    if S[i]=='o':
        A[i+1][0]=A[i][0]+1
        A[i+1][1]=A[i][1]
    else:
        A[i+1][0]=A[i][0]
        A[i+1][1]=A[i][1]+1

l=0
ans=0
for r in range(N+1):
    while l<r and A[r][0]-A[l][0]>0 and A[r][1]-A[l][1]>0:
        ans+=N-r+1
        l+=1
print(ans)
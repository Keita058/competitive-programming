import bisect

N,M=map(int,input().split())
A=list(map(int,input().split()))
A.sort()

ans=0
for i in range(N):
    x=A[i]
    y=bisect.bisect_left(A,x+M-0.5)
    ans=max(ans,y-i)
print(ans)
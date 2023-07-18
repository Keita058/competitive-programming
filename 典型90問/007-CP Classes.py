from bisect import bisect_left

N=int(input())
A=list(map(int,input().split()))
A.sort()
ans=0

Q=int(input())
for _ in range(Q):
    B=int(input())
    index=bisect_left(A,B)
    if index==0:
        ans=abs(A[index]-B)
    elif index==N:
        ans=abs(A[index-1]-B)
    else:
        ans=min(abs(A[index]-B),abs(A[index-1]-B))
    print(ans)
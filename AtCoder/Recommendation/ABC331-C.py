import bisect

N=int(input())
A=list(map(int,input().split()))
A_sort=sorted(A)
B=[0]*(N+1)
for i in range(N):
    B[i+1]=B[i]+A_sort[i]

ans=[]

for i in range(N):
    id=bisect.bisect_right(A_sort,A[i])
    ans.append(B[N]-B[id])

print(*ans)
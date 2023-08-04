#典型90-046類題
#problem URL :https://atcoder.jp/contests/arc115/tasks/arc115_c

N=int(input())
A=[1 for _ in range(N+1)]
for i in range(1,N+1):
    k=2
    while i*k<=N:
        A[i*k]=max(A[i*k],A[i]+1)
        k+=1
print(*A[1:])
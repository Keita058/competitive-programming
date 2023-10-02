import bisect

N,M=map(int,input().split())
A=list(map(int,input().split()))

for i in range(N):
    ans_id=bisect.bisect_left(A,i+1)
    ans=A[ans_id]
    print(ans-(i+1))
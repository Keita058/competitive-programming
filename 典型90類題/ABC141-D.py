#典型90-046類題
#problem URL :https://atcoder.jp/contests/abc141/tasks/abc141_d

import heapq

N,M=map(int,input().split())
A=list(map(int,input().split()))
for i in range(N):
    A[i]*=-1
heapq.heapify(A)
for i in range(M):
    a=-heapq.heappop(A)//2
    heapq.heappush(A,-a)
ans=-1*sum(A)
print(ans)
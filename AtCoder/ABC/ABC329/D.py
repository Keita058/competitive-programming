import heapq

N,M=map(int,input().split())
A=list(map(int,input().split()))

ans=[[] for _ in range(M+1)]
for i in range(N):
    ans[0].append(i+1)
B=[0 for _ in range(N+1)]

MAX=0
for i in range(M):
    B[A[i]]+=1
    ans[B[A[i]]].append(A[i])
    MAX=max(MAX,B[A[i]])
    x=ans[MAX]
    heapq.heapify(x)
    y=heapq.heappop(x)
    print(y)
    x.append(y)
from collections import deque

N=int(input())
G=[[] for _ in range(N)]
for i in range(N-1):
    a,b=map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

dist=[float('inf') for _ in range(N)]
dist[0]=0
nv=deque([0])
visited=[False for _ in range(N)]
while nv:
    v=nv.popleft()
    visited[v]=True
    for u in G[v]:
        if visited[u]:
            continue
        dist[u]=dist[v]+1
        nv.append(u)

max_dist=max(dist)
nu=0
for i in range(N):
    if dist[i]==max_dist:
        nu=i

dist=[float('inf') for _ in range(N)]
dist[nu]=0
nv=deque([nu])
visited=[False for _ in range(N)]
while nv:
    v=nv.popleft()
    visited[v]=True
    for u in G[v]:
        if visited[u]:
            continue
        dist[u]=dist[v]+1
        nv.append(u)
print(max(dist)+1)
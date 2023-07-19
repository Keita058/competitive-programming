N,M=map(int,input().split())
G=[0 for _ in range(N)]
for _ in range(M):
    a,b=map(int,input().split())
    if a<b:
        G[b-1]+=1
    else:
        G[a-1]+=1

print(G.count(1))
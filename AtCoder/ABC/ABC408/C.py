N,M=map(int,input().split())

wall=[0 for _ in range(N+1)]
for _ in range(M):
    l,r=map(int,input().split())
    wall[l-1]+=1
    wall[r]-=1

for i in range(1,N):
    wall[i]+=wall[i-1]

print(min(wall[:N]))
import sys
sys.setrecursionlimit(10**7)

H,W=map(int,input().split())
G=list()
for i in range(H):
    s=input()
    G.append(list(s))

dxy=[(1,0),(-1,0),(0,1),(0,-1)]
for i in range(H):
    for j in range(W):
        if G[i][j]=="#":
            continue
        for dx,dy in dxy:
            ni,nj=i+dx,j+dy
            if ni<0 or ni>=H or nj<0 or nj>=W:
                continue
            if G[ni][nj]=="#":
                G[i][j]="x"

visited=[[False]*W for _ in range(H)]

def dfs(x,y,m_set,cnt):
    if visited[x][y]:
        return
    visited[x][y]=True
    cnt+=1
    for dx,dy in dxy:
        nx,ny=x+dx,y+dy
        if nx<0 or nx>=H or ny<0 or ny>=W:
            continue
        if G[nx][ny]=="x":
            m_set.add((nx,ny))
            continue

        dfs(nx,ny,m_set,cnt)

ans=0
for i in range(H):
    for j in range(W):
        if G[i][j]=="." and not visited[i][j]:
            m_set=set()
            cnt=0
            dfs(i,j,m_set,cnt)
print(ans)
N,X,Y=map(int,input().split())

jewels=[[0,0] for _ in range(N+1)] #[level, red, blue]
jewels[N][0]=1

for i in range(N,1,-1):
    jewels[i-1][0]+=jewels[i][0]
    jewels[i][1]+=jewels[i][0]*X
    jewels[i][0]=0
    jewels[i-1][0]+=jewels[i][1]
    jewels[i-1][1]+=jewels[i][1]*Y
    jewels[i][1]=0

print(jewels[1][1])
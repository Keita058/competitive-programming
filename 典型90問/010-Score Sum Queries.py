N=int(input())
dp=[[0, 0] for _ in range(N+1)]
for i in range(N):
    c,p=map(int,input().split())
    dp[i+1][c-1]=p

for i in range(N):
    for j in range(2):
        dp[i+1][j]+=dp[i][j]

Q=int(input())
for _ in range(Q):
    l,r=map(int,input().split())
    print(dp[r][0]-dp[l-1][0], dp[r][1]-dp[l-1][1])
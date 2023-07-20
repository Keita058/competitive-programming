N,L=map(int,input().split())
dp=[0 for _ in range(N+1)]
dp[0]=1
#dp[i]:=i団目に到達する上り方の総数
for i in range(N):
    dp[i+1]+=dp[i]
    if i+L<=N:
        dp[i+L]+=dp[i]
MOD=10**9+7
print(dp[N]%MOD)
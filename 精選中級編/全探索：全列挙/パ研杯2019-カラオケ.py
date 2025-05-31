#https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_c
N,M=map(int,input().split())
A=[list(map(int,input().split())) for i in range(N)]

ans=0
for x in range(M-1):
    for y in range(x+1,M):
        s=0
        for i in range(N):
            s+=max(A[i][x],A[i][y])
        ans=max(ans,s)
print(ans)
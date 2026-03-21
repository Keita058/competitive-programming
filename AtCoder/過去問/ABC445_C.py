N=int(input())
A=list(map(int(input().split())))
flag=[False for _ in range(N)]

for i in range(N):
    if flag[i]:
        continue

n=int(input())
ans=[[[0 for _ in range(10)] for _ in range(3)] for _ in range(4)]
for _ in range(n):
    b,f,r,v=map(int,input().split())
    ans[b-1][f-1][r-1]+=v

for i in range(4):
    for j in range(3):
        s=""
        for k in range(10):
            print(' ', ans[i][j][k], sep='', end='')
        print()
    if i<3:
        print("#"*20, end="")
        print()
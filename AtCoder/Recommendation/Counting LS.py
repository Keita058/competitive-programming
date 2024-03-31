N=int(input())
G=[]
for i in range(N):
    S=input()
    G.append(list(S))

row=[[0 for _ in range(N)] for _ in range(N)] # row[i][j]: i行目のj列から見たi行目の他のoの数
col=[[0 for _ in range(N)] for _ in range(N)] # col[i][j]: i列目のj行から見たj列目の他のoの数

for i in range(N):
    #i行目について
    col_i=0
    for j in range(N):
        #j列目について
        if G[i][j]=='o':
            col_i+=1
    for j in range(N):
        if G[i][j]=='o':
            col[i][j]=col_i-1
        else:
            col[i][j]=col_i

for j in range(N):
    #j列目について
    row_j=0
    for i in range(N):
        #i行目について
        if G[i][j]=='o':
            row_j+=1
    for i in range(N):
        if G[i][j]=='o':
            row[i][j]=row_j-1
        else:
            row[i][j]=row_j

#(i,j)のoを取るとき，他の2つのoの取り方は，row[i][j]とcol[j][i]の積
#(i,j)!=(s,t)のとき，数え方は重複しない
ans=0
for i in range(N):
    for j in range(N):
        if G[i][j]=='o':
            ans+=row[i][j]*col[i][j]

print(ans)
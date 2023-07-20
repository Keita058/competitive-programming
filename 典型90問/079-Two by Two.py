H,W=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(H)]
B=[list(map(int,input().split())) for _ in range(H)]

#左上から合わせて行ってx,y=H-1,W-1を変えた時にA=Bかどうかで判定
ans=0
for i in range(H-1):
    for j in range(W-1):
        dif=B[i][j]-A[i][j]
        ans+=abs(dif)
        A[i][j]+=dif
        A[i+1][j]+=dif
        A[i][j+1]+=dif
        A[i+1][j+1]+=dif

if A==B:
    print('Yes')
    print(ans)
else:
    print('No')
N=int(input())

if N%2==1:
    print()
    exit()

ans=[[] for _ in range(N+1)]
ans[2].append('()')


for k in range(0,N+1,2):
    #長さkの正しいカッコ列Sをk-2以下の長さのカッコ列から求める
    for i in range(0,k+1,2):
        #長さiのカッコ列Tと長さk-iのカッコ列T'からSを創る
        if len(ans[i])==0 or len(ans[k-i])==0:
            continue
        for m in range(len(ans[i])):
            if i==k-2:
                ans[k].append('('+ans[i][m]+')')
            for n in range(len(ans[k-i])):
                    ans[k].append(ans[i][m]+ans[k-i][n])
    ans[k]=sorted(set(ans[k]))

for x in ans[N]:
    print(x)
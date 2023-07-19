def base8to10(x):
    #xは1の位から順に並べられた整数のリスト
    #戻り値は10進数の整数
    m=len(x)
    res=0
    for i in range(m):
        res+=x[i]*8**i
    return res

def base10to9(x):
    #xは10進数の整数
    #戻り値は8進数の1の位から順に並べた整数のリスト
    res=list()
    while x>0:
        c=x%9
        if c==8:
            c=5
        res.append(c)
        x=(x-c)//9
    return res

N,K=map(int,input().split())

base8=list(str(N))[::-1]

for i in range(len(base8)):
    base8[i]=int(base8[i])

for i in range(K):
    base10=base8to10(base8)
    base8=base10to9(base10)

ans=0
for i in range(len(base8)):
    ans+=base8[i]*10**i
print(ans)
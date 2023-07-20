def sums(A,B):
    #A以上B以下の整数の和を返す
    return (B+A)*(B-A+1)//2

MOD=10**9+7
L,R=map(int,input().split())

ans=0
for i in range(1,20):
    if 10**(i-1)<=L<10**i and R<10**i:
        ans+=i*sums(L,R)
        break
    elif 10**(i-1)<=L<10**i:
        ans+=i*sums(L,10**i-1)
    elif L<10**(i-1) and 10**i<=R:
        ans+=i*sums(10**(i-1),10**i-1)
    elif L<10**(i-1) and R<10**i:
        ans+=i*sums(10**(i-1),R)
        break
print(ans%MOD)
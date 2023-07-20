MOD=10**9+7

N,K=map(int,input().split())

ans=K
if N>2:
    ans*=(K-1)*pow(K-2,N-2,MOD)
elif N==2:
    ans*=K-1

print(ans%MOD)
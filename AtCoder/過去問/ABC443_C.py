N,T=map(int,input().split())
A=list(map(int,input().split()))

ct=0
lt=-100

for i in range(N):
    if lt+100>A[i]:
        continue
    lt=A[i]
    if lt+100>T:
        ct+=(T-lt)
    else:
        ct+=100

print(T-ct)
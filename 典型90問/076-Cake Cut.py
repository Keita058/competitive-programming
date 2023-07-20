N=int(input())
A=list(map(int,input().split()))
size=sum(A)
A=A+A
B=[0 for _ in range(2*N+1)]
for i in range(2*N):
    B[i+1]=B[i]+A[i]

flag=False
r=0
for l in range(2*N+1):
    while (B[r]-B[l])*10<size and r<2*N:
        r+=1
    if (B[r]-B[l])*10==size:
        flag=True
        break

print('Yes' if flag else 'No')
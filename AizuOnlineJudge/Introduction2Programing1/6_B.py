n=int(input())
S=[0 for _ in range(13)]
H=[0 for _ in range(13)]
C=[0 for _ in range(13)]
D=[0 for _ in range(13)]
for i in range(n):
    a,b=input().split()
    b=int(b)
    if a=="S":
        S[b-1]=1
    elif a=="H":
        H[b-1]=1
    elif a=="C":
        C[b-1]=1
    else:
        D[b-1]=1

ans=[]
for i in range(13):
    if S[i]==0:
        ans.append(["S", i+1])
for i in range(13):
    if H[i]==0:
        ans.append(["H", i+1])
for i in range(13):
    if C[i]==0:
        ans.append(["C", i+1])
for i in range(13):
    if D[i]==0:
        ans.append(["D", i+1])

for i in range(len(ans)):
    print(*ans[i])
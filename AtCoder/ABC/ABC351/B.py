N=int(input())
A=list()
B=list()

for i in range(N):
    s=input()
    A.append(s)

for i in range(N):
    t=input()
    B.append(t)

ans=[0,0]
for i in range(N):
    s,t=A[i],B[i]
    for j in range(N):
        if s[j]!=t[j]:
            ans=[i+1,j+1]
            break

print(*ans)
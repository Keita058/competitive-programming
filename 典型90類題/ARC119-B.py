#典型90-046類題
#problem URL :https://atcoder.jp/contests/arc119/tasks/arc119_b

N=int(input())
S=input()
T=input()

A=[]
B=[]
for i in range(N):
    if S[i]=='0':
        A.append(i)
    if T[i]=='0':
        B.append(i)

if len(A)==len(B):
    ans=0
    for i in range(len(A)):
        if A[i]!=B[i]:
            ans+=1
    print(ans)
else:
    print(-1)
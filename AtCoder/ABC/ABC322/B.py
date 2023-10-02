N,M=map(int,input().split())
S=input()
T=input()

S_rev=S[::-1]
T_rev=T[::-1]

flag=True
flag_rev=True

for i in range(N):
    if S[i]!=T[i]:
        flag=False
    if S_rev[i]!=T_rev[i]:
        flag_rev=False

if flag and flag_rev:
    print(0)
elif flag:
    print(1)
elif flag_rev:
    print(2)
else:
    print(3)
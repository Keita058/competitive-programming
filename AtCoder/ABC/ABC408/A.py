N,S=map(int,input().split())
T=list(map(int,input().split()))

flag=True
for i in range(N):
    if i==0:
        if T[i]>S:
            flag=False
    else:
        if T[i]>T[i-1]+S:
            flag=False
if flag:
    print("Yes")
else:
    print("No")
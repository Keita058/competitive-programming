#https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_d
N=int(input())
S=input()

ans=0
for x in range(1000):
    if x<10:
        key='00'+str(x)
    elif x<100:
        key='0'+str(x)
    else:
        key=str(x)
    cnt=0
    for i in range(N):
        if S[i]==key[cnt]:
            cnt+=1
        if cnt==3:
            break
    if cnt==3:
        ans+=1
print(ans)
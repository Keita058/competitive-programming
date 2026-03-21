N=int(input())
m=0
ss=list()
for _ in range(N):
    s=input()
    ss.append(s)
    m=max(m, len(s))

for i in range(N):
    s=ss[i]
    l=len(s)
    k=(m-l)//2
    t='.'*k
    ans=t+s+t
    print(ans)

H,W,N=map(int,input().split())

a,b=list(),list()
for _ in range(N):
    x,y=map(int,input().split())
    a.append(x)
    b.append(y)
a_set,b_set=sorted(set(a)),sorted(set(b))
a_dict,b_dict=dict(),dict()
for i in range(len(a_set)):
    a_dict[a_set[i]]=i+1
for i in range(len(b_set)):
    b_dict[b_set[i]]=i+1

ans=[0 for _ in range(N)]
for i in range(N):
    ans[i]=(a_dict[a[i]],b_dict[b[i]])

for i in range(N):
    print(*ans[i])
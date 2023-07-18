def bisect(ng, ok):
    while abs(ng-ok)>1:
        mid=(ng+ok)//2
        if is_ok(mid):
            ok=mid
        else:
            ng=mid
    return ok

def is_ok(x):
    last=0
    cnt=0
    for i in range(N+1):
        if A[i]-last>=x:
            cnt+=1
            last=A[i]
    return cnt>K

N,L=map(int,input().split())
K=int(input())
A=list(map(int,input().split()))
A.append(L)

cut_len=bisect(L+1,0)
ans=float('inf')
last=0
for i in range(N+1):
    if A[i]-last>=cut_len:
        ans=min(A[i]-last,ans)
        last=A[i]

print(ans)
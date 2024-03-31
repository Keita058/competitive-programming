N,M=map(int,input().split())
L=list(map(int,input().split()))

def meguru_bisect(ng,ok):
    mid=(ng+ok)//2
    while (abs(ng-ok)>1):
        if checker(N,M,mid):
            ok=mid
        else:
            ng=mid
        mid=(ng+ok)//2
    return ok

def checker(n, m, w):
    cnt = 0
    col=1
    for i in range(n):
        if L[i]>w:
            col=float('inf')
            break
        if cnt+L[i]>w:
            col+=1
            cnt=0
        cnt += L[i]+1
    if col>m:
        return False
    else:
        return True

print(meguru_bisect(0,10**11))
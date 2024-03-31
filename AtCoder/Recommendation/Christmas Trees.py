A,M,L,R=map(int,input().split())

def is_ok(x, side):
    # 条件を満たすかどうか？問題ごとに定義
    return A+x*M>=side

def meguru_bisect(ng,ok,side):
    while abs(ok-ng)>1:
        mid=(ok+ng)//2
        if is_ok(mid,side):
            ok=mid
        else:
            ng=mid
    return ok

L_x=meguru_bisect(-10**19,10**19,L)
R_x=meguru_bisect(-10**19,10**19,R)
print(R_x-L_x)
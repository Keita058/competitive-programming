while True:
    n=int(input())
    if n==0:
        break
    S=list(map(int,input().split()))
    m=sum(S)/n
    sgm=0
    for i in range(n):
        sgm+=(S[i]-m)**2
    sgm=(sgm/n)**0.5
    print(round(sgm,5))
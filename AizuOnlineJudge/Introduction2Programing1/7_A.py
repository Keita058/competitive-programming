while True:
    m,f,r=map(int,input().split())
    if m==-1 and f==-1 and r==-1:
        break
    score=m+f
    ans=""
    if m==-1 or f==-1:
        ans="F"
    elif score>=80:
        ans="A"
    elif score>=65:
        ans="B"
    elif score>=50:
        ans="C"
    elif score>=30:
        if r>=50:
            ans="C"
        else:
            ans="D"
    else:
        ans="F"
    print(ans)
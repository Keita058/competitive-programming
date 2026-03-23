while True:
    x=input()
    if x=="-":
        break
    m=int(input())
    for j in range(m):
        h=int(input())
        a=x[h:]
        b=x[:h]
        x=a+b
    print(x)
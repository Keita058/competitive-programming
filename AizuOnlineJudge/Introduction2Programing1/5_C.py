while True:
    h,w=map(int,input().split())
    if h==0 and w==0:
        break
    for i in range(h):
        t=""
        for j in range(w):
            if i%2==j%2:
                t+="#"
            else:
                t+="."
        print(t)
    print()
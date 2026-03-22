while True:
    h,w=map(int,input().split())
    if h==0 and w==0:
        break
    for i in range(1,h+1):
        if i==1 or i==h:
            print("#"*w)
        else:
            print("#"+"."*(w-2)+"#")
    print()
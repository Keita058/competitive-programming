n=int(input())
x,y=0,0
for _ in range(n):
    a,b=input().split()
    if a<b:
        y+=3
    elif a>b:
        x+=3
    else:
        x+=1
        y+=1
print(x,y)
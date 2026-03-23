n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))

def dist(x,y,p):
    m=len(x)
    ret=0
    for i in range(m):
        ret+=abs(x[i]-y[i])**p
    ret=ret**(1/p)
    return ret

for i in range(1,4):
    print(round(dist(x,y,i),6))

cd=0
for i in range(n):
    cd=max(cd,abs(x[i]-y[i]))
print(round(cd,6))
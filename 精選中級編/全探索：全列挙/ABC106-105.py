N=int(input())
ans=0
for x in range(1,N+1):
    if x%2==0:
        continue
    cnt=0
    i=1
    while i*i<=x:
        if x%i==0:
            cnt+=1
            if i!=x//i:
                cnt+=1
        i+=1
    if cnt==8:
        ans+=1
print(ans)
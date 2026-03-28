N,A,B=map(int,input().split())

ans=0
for i in range(N+1):
    s=str(i)
    cnt=0
    for j in range(len(s)):
        cnt+=int(s[j])
    if A<=cnt and cnt<=B:
        ans+=i
print(ans)
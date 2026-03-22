n=int(input())
ans=[]
for i in range(1,n+1):
    if i%3==0:
        ans.append(i)
    elif "3" in str(i):
        ans.append(i)

print(*ans)

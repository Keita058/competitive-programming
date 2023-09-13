N,M=map(int,input().split())
a=list(map(int,input().split()))
a=set(a)

stack=[]
ans=[]
for i in range(N):
    stack.append(i+1)
    if i+1 in a:
        pass
    else:
        while stack:
            ans.append(stack.pop())
print(*ans)
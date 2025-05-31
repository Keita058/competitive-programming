N=int(input())
A=list(map(int,input().split()))

ans=[]
for i in range(N):
    ans.append(A[i])
    while len(ans)>=2:
        f,s=ans[-1],ans[-2]
        if f==s:
            ans.pop()
            ans.pop()
            ans.append(f+1)
        else:
            break
print(len(ans))
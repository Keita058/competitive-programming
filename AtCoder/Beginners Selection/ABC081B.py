def div2(x,ret=0):
    if x%2==0:
        ret+=1
        return div2(x//2,ret)
    else:
        return ret

N=int(input())
A=list(map(int,input().split()))
ans=10**9
for i in range(N):
    ans=min(ans, div2(A[i]))
print(ans)
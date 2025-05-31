#https://atcoder.jp/contests/abc095/tasks/arc096_a
A,B,C,X,Y=map(int,input().split())
ans=float('inf')

for i in range(2*max(X,Y)+1):
    if i%2==1:
        continue
    j=max(X-i//2,0)
    k=max(Y-i//2,0)
    ans=min(ans,A*j+B*k+C*i)
print(ans)
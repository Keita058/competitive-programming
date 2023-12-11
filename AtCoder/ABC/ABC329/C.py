N=int(input())
S=input()

ans=set()
l=0
for r in range(N):
    if S[l]==S[r]:
        ans.add((S[l],r-l+1))
    else:
        ans.add((S[r],1))
        l=r

if S[l]==S[N-1]:
    ans.add((S[l],N-l))
else:
    ans.add((S[N-1],1))

print(len(ans))
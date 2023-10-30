N,M=map(int,input().split())
A=list(map(int,input().split()))
S=[input() for _ in range(N)]
now_score=[]
for i in range(N):
    cnt=i+1
    for j in range(M):
        if S[i][j]=='o':
            cnt+=A[j]
    now_score.append(cnt)
now_max=max(now_score)

B=[]
for i in range(M):
    B.append((A[i],i))
B.sort()

def func(score,p_num,prob):
    cnt=0
    while score<now_max:
        s,prob_num=prob.pop()
        if S[p_num][prob_num]=='o':
            continue
        score+=s
        cnt+=1
    return cnt

for i in range(N):
    B_dash=B.copy()
    now=now_score[i]
    ans=func(now,i,B_dash)
    print(ans)
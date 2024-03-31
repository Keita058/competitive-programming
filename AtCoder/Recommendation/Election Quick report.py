N,M=map(int,input().split())
A=list(map(int,input().split()))
Voted=[0 for _ in range(N)]
now_id=0
now_voted=0

for i in range(M):
    Voted[A[i]-1]+=1
    if now_voted<Voted[A[i]-1]:
        now_voted=Voted[A[i]-1]
        now_id=A[i]
    elif now_voted==Voted[A[i]-1]:
        if now_id>A[i]:
            now_id=A[i]
    print(now_id)
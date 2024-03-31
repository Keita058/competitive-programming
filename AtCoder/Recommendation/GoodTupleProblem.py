N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

AB=[]
for i in range(N):
    if A[i]==B[i]:
        print('No')
        exit()
    else:
        AB.append((min(A[i],B[i]),max(A[i],B[i])))
AB=sorted(set(AB))

G=[[] for _ in range(N)]
for a,b in AB:
    G[a-1].append(b-1)
    G[b-1].append(a-1)


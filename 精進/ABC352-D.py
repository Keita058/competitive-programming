N,K=map(int,input().split())
P=list(map(int,input().split()))

Q=[(P[i],i) for i in range(N)]
Q.sort()
print(Q)


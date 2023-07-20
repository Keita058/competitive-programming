N,K=map(int,input().split())
G=[]
for i in range(N):
    a,b=map(int,input().split())
    G.append(b)
    G.append(a-b)

G.sort()
G.reverse()
print(sum(G[:K]))
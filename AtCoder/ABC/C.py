H,W=map(int,input().split())
S=[[] for _ in range(H)]
for i in range(H):
    t=input()
    for j in range(W):
        S[i].append(t[j])


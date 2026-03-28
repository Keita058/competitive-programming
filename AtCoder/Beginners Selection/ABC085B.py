N=int(input())
A=[]
for _ in range(N):
    d=int(input())
    A.append(d)
print(len(set(A)))
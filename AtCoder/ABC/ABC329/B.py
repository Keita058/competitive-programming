N=int(input())
A=list(map(int,input().split()))

A_set=sorted(set(A))
print(A_set[-2])
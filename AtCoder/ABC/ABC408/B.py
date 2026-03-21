N=int(input())
A=list(map(int,input().split()))

A_set=list((set(A)))
A_set.sort()

print(len(A_set))
print(*A_set)
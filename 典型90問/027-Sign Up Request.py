N=int(input())
name_set=set()
for i in range(N):
    s=input()
    if s in name_set:
        continue
    print(i+1)
    name_set.add(s)
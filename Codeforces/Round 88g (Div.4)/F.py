from collections import defaultdict

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a_dict=defaultdict(int)
    for i in range(n):
        a_dict[a[i]]+=1
    A_set=sorted(set(a))
    M=len(A_set)
    nums=[0 for _ in range(n+1)]
    for x in A_set:
        if x>n:
            break
        y=1
        while x*y<=n:
            nums[x*y]+=a_dict[x]
            y+=1
    print(max(nums))
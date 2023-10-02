t=int(input())
for _ in range(t):
    n=int(input())
    S_set=set()
    S_list=[]
    k_list=[]
    for i in range(n):
        S=list(map(int,input().split()))
        k,S=S[0],S[1:]
        S_list.append(S)
        k_list.append(k)
        for j in range(k):
            S_set.add(S[j])
    ans=0
    for i in range(2**n):
        ans_set=set()
        for j in range(n):
            if((i>>j)&1):
                for l in range(k_list[j]):
                    ans_set.add(S_list[j][l])
        if(ans_set==S_set):
            continue
        ans=max(ans,len(ans_set))
    print(ans)
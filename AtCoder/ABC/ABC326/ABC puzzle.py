from itertools import permutations

N=int(input())
R=input()
C=input()

arr=[i for i in range(N)]
v=list(permutations(arr))

def check_1(Grid,N):
    ABC_cnt=[[0,0,0] for _ in range(N)]
    for i in range(N): #i:列
        for j in range(N): #j:行
            if Grid[i][j]=="A":
                ABC_cnt[i][0]+=1
            elif Grid[i][j]=="B":
                ABC_cnt[i][1]+=1
            elif Grid[i][j]=="C":
                ABC_cnt[i][2]+=1
    res_flag=True
    for i in range(N):
        for j in range(3):
            if ABC_cnt[i][j]!=1:
                res_flag=False
                break
    return res_flag

def check_2(Grid,N,R):
    for i in range(N):
        for j in range(N):
            if Grid[i][j]!='.':
                if Grid[i][j]!=R[i]:
                    return False
                else:
                    break
    return True

def check_3(Grid,N,C):
    for i in range(N):
        for j in range(N):
            if Grid[j][i]!='.':
                if Grid[j][i]!=C[i]:
                    return False
                else:
                    break
    return True

for ap in v:
    for bp in v:
        for cp in v:
            flag=False
            for i in range(N):
                if ap[i]==bp[i] or bp[i]==cp[i] or cp[i]==ap[i]:
                    flag=True
                    break
            if flag:
                continue
            G_dash=[['.' for _ in range(N)] for _ in range(N)]
            for i in range(N):
                G_dash[i][ap[i]]='A'
                G_dash[i][bp[i]]='B'
                G_dash[i][cp[i]]='C'
            if check_1(G_dash,N) and check_2(G_dash,N,R) and check_3(G_dash,N,C):
                print('Yes')
                for i in range(N):
                    print(''.join(G_dash[i]))
                exit()

print('No')
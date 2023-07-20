N=int(input())
G=[list(map(int,input().split())) for _ in range(3)]
A,B,C=G[0],G[1],G[2]

A_dict={i:0 for i in range(46)}
B_dict={i:0 for i in range(46)}
C_dict={i:0 for i in range(46)}

for i in range(N):
    a,b,c=A[i]%46,B[i]%46,C[i]%46
    A_dict[a]+=1
    B_dict[b]+=1
    C_dict[c]+=1

ans=0
for i in range(46):
    #Aの数字を46で割った余りがiの時
    for j in range(46):
        #Bの数字を46で割った余りがjの時
        k=(46-i-j)%46
        ans+=A_dict[i]*B_dict[j]*C_dict[k]
print(ans)
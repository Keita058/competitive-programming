s=input()
q=int(input())
for _ in range(q):
    t=input()
    A=t.split()
    if A[0]=="replace":
        a,b,p=int(A[1]), int(A[2]), A[3]
        i,j,k=s[:a],s[a:b+1],s[b+1:]
        s=i+p+k
    elif A[0]=="reverse":
        a,b=int(A[1]), int(A[2])
        i,j,k=s[:a],s[a:b+1],s[b+1:]
        s=i+j[::-1]+k
    else:
        a,b=int(A[1]), int(A[2])
        print(s[a:b+1])
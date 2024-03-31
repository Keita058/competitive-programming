S=input()
N=len(S)
arr=[]

for i in range(N):
    t=S[i]
    if t=='C' and len(arr)>=2:
        X2=arr.pop()
        X1=arr.pop()
        if X1=='A' and X2=='B':
            continue
        else:
            arr.append(X1)
            arr.append(X2)
            arr.append(t)
    else:
        arr.append(t)

print(''.join(arr))
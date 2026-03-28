S=input()
Words=set(['dream', 'dreamer', 'erase', 'eraser'])
while len(S)>0:
    if S[-5:] in Words:
        S=S[:-5]
    elif S[-6:] in Words:
        S=S[:-6]
    elif S[-7:] in Words:
        S=S[:-7]
    else:
        print('NO')
        exit()
print('YES')
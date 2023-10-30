S=input()
S=list(S)

while True:
    S.pop()
    if len(S)%2==0:
        if S[:len(S)//2]==S[len(S)//2:]:
            print(len(S))
            exit()
C=input()
alp="abcdefghijklmnopqrstuvwxyz"

for i in range(len(alp)):
    if alp[i]==C:
        print(alp[i+1])
        exit()
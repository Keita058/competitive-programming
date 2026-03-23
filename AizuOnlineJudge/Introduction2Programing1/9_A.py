W=input()
T=[]
while True:
    s=input().split()
    if s==["END_OF_TEXT"]:
        break
    for x in s:
        T.append(x.lower())

ans=0
for x in T:
    if x==W:
        ans+=1
print(ans)
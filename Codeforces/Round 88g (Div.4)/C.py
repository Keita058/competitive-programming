t=int(input())
for _ in range(t):
    ans=''
    for i in range(8):
        s=input()
        for x in s:
            if x!='.':
                ans+=x
    print(ans)
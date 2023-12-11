from collections import deque

def main():
    Q=int(input())
    MOD=998244353
    S=deque([1])
    ans=1
    for _ in range(Q):
        query=list(map(int,input().split()))
        if query[0]==1:
            x=query[1]
            S.append(x)
            ans=10*ans+x
        elif query[0]==2:
            y=S.popleft()
            ans=ans-pow(10,len(S))*y
        else:
            print(ans%MOD)


if __name__ == '__main__':
    main()
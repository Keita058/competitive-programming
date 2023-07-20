def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr

N=int(input())
num_prime=0
for i,j in factorization(N):
    num_prime+=j
for i in range(48):
    if num_prime<=2**i:
        ans=i
        break
print(ans)
#x以下の素数を列挙するプログラム


def sieve_of_eratosthenes(x):
    nums=[i for i in range(x+1)]
    root=int(x**0.5)
    for i in range(2,root+1):
        if nums[i]!=0:
            for j in range(i,x+1):
                if i*j>=x+1:
                    break
                nums[i*j]=0
    primes=sorted(list(set(nums[2:])))
    return primes

p=sieve_of_eratosthenes(int(10**(9/2)+1))
print(len(p))
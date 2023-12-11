#N以下の正の整数をすべて素因数分解するプログラム
#計算量はO(NloglogN)

class osa_k:
    def __init__(self,nmax):
        self.min_factor=[i for i in range(nmax+1)]

        i=2
        while i*i<=nmax:
            if self.min_factor[i]==i:
                j=i*2
                while j<=nmax:
                    if self.min_factor[j]>i:
                        self.min_factor[j]=i
                    j+=i
            i+=1
    
    def factorization(self,M):
        factDict=dict()
        while M>1:
            p=self.min_factor[M]
            if p not in factDict:
                factDict[p]=1
            else:
                factDict[p]+=1
            M//=p
        
        res=[(fact,order) for fact,order in factDict.items()]
        return res
    
    def num_of_factor(self,nmax):
        res=[1]*(nmax+1)
        res[0]=0
        for i in range(2,nmax+1):
            facts=self.factorization(i)
            for fact,order in facts:
                res[i]*=order+1
        return res
    

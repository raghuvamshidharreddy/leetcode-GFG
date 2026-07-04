class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        def primesList(n):
            seive=[True]*(n+1)
            seive[0]=seive[1]=False
            for i in range(2,int(n**0.5)+1):
                if seive[i]:
                    for j in range(i*i,n+1,i):
                        seive[j]=False
            li=[]
            for i in range(2,len(seive)):
                if seive[i]:
                    li.append(i)
            return li
        primes=primesList(n)
        ans=[]
        i,j=0,len(primes)-1
        while(i<=j):
            if(primes[i]+primes[j]==n):
                ans.append([primes[i],primes[j]])
                i+=1
            elif(primes[i]+primes[j]>n):
                j-=1
            else:
                i+=1
        return ans

